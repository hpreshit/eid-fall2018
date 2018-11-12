#Created by - Preshit Harlikar and Smitesh Modak
#Date - 10/21/2018

import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import QDialog, QApplication

from SensorUI import Ui_SensorInterface

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import Adafruit_DHT

import sqlite3

import time

import boto3
from config_aws import *

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        #integrating the UI
        self.ui = Ui_SensorInterface()
        self.ui.setupUi(self)

        #global variables
        global unit, count, tempAvg, humAvg, samples, tempArr, humArr, timerflag, tempLimit, humLimit, tempHigh, tempLow, humHigh, humLow, temp, connection, crsr
        unit = 1
        count,tempAvg,humAvg,samples,timerflag,tempHigh,humHigh = 0,0,0,0,0,0,0
        tempLow, humLow = 500, 500
        tempArr = [None]*10
        humArr = [None]*10
        tempLimit = 100
        humLimit = 100

        #initialize database
        connection = sqlite3.connect("localdht.db")
        crsr = connection.cursor()

        #initializing timer
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.getTempHum)

        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.celciusButton.clicked.connect(self.celciusTemp)
        self.ui.fahrenheitButton.clicked.connect(self.fahrenheitTemp)
        self.ui.timerButton.clicked.connect(self.timerStartStop)
        self.ui.resetButton.clicked.connect(self.resetAvg)
        self.ui.graphButton.clicked.connect(self.graphTempHum)
        self.ui.tempDial.valueChanged.connect(self.setTempLimit)
        self.ui.humDial.valueChanged.connect(self.setHumLimit)
        self.ui.cleardatabaseButton.clicked.connect(self.clearDB)

        global sqs, test_queue_url
        sqs = boto3.client('sqs', region_name=''.join(region),
                   aws_access_key_id =''.join(access_key_id),
                   aws_secret_access_key =''.join(secret_access_key))

        test_queue_url = ''.join(queue_url)

        #function to get temp and humidity from the sensor
    def getTempHum(self):
        global unit, count, tempAvg, humAvg, tempHigh, tempLow, humHigh, humLow, tempArr, humArr, samples, tempLimit, humLimit, temp, connection, crsr
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

        global temp3, temp4, hum3, hum4
        #create table
        crsr.execute("CREATE TABLE IF NOT EXISTS DHT_DATA(Timestamp TEXT,Temperature numeric(3,1),Unit TEXT,Average_Temperature numeric(3,1),High_Temperature numeric(3,1),Low_Temperature numeric(3,1),Humidity numeric(3,1),Average_Humidity numeric(3,1),High_Humidity numeric(3,1),Low_Humidity numeric(3,1))")

        #check if sensor is disconnected
        if humidity is None and temperature is None:
            self.ui.alertDisplay.setText(" SENSOR DISCONNECTED")
            self.ui.temperatureDisplay.display("")
            self.ui.humidityDisplay.display("")
            self.ui.temperatureAvgDisplay.display("")
            self.ui.humidityAvgDisplay.display("")
            self.ui.sensorStatus.setStyleSheet("background-color: rgb(255, 0, 0);")

            #update the time of request for tem and humidity values
            newtime = time.strftime('%m-%d-%y  %H:%M:%S')
##            self.ui.timeDisplay.setText(newtime)
            self.ui.timeDisplay.setText(time_stamp[len(temp_value)-1])

            temp1,tempUnit,temp2,temp3,temp4,hum1,hum2,hum3,hum4time = 0,0,0,0,0,0,0,0,0
            #update database
            crsr.execute("INSERT INTO dht_data values(?,?,?,?,?,?,?,?,?,?)",(newtime,temp1,tempUnit,temp2,temp3,temp4,hum1,hum2,hum3,hum4time))
            connection.commit()

        else:
            self.ui.sensorStatus.setStyleSheet("background-color: rgb(0, 255, 0);")
            count = count + 1

            tempUnit = "°C"
            #conversion from cecius to fahrenheit
            if unit == 0:
                # temperature = (temperature*1.8) + 32
                temperature = (temp_value(len(temp_value)-1)*1.8) + 32
                tempUnit = "°F"

            #display current temp and humidity value on LCD Display
            temp1 = '{0:.2f}'.format(temperature)
##            self.ui.temperatureDisplay.display(temp1)
            self.ui.temperatureDisplay.display(temp_value(len(temp_value)-1))
            hum1 = '{0:.2f}'.format(humidity)
##            self.ui.humidityDisplay.display(hum1)
            self.ui.humidityDisplay.display(hum_value(len(hum_value)-1))


            #Set an alert for high temperautre
            if temperature > tempLimit:
                self.ui.alertDisplay.setText("    HIGH TEMPERATURE")
            elif humidity > humLimit:
                self.ui.alertDisplay.setText("        HIGH HUMIDITY")
            else:
                self.ui.alertDisplay.setText("")

            #calculating average temperature and humidity continuously for each sample
            tempAvg=((tempAvg * (count-1)) + temperature) / count
            temp2 = '{0:.2f}'.format(tempAvg)
##            self.ui.temperatureAvgDisplay.display(temp2)
            self.ui.temperatureAvgDisplay.display(temp_avg(len(temp_avg)-1))
            humAvg=((humAvg * (count-1)) + humidity) / count
            hum2 = '{0:.2f}'.format(humAvg)
##            self.ui.humidityAvgDisplay.display(hum2)
            self.ui.humidityAvgDisplay.display(hum_avg(len(hum_avg)-1))

            # if temperature > tempHigh:
            #     tempHigh = temperature
            #     temp3 = '{0:.2f}'.format(tempHigh)
            #     self.ui.temperatureHighDisplay.display(temp3)
            #
            # if temperature < tempLow:
            #     tempLow = temperature
            #     temp4 = '{0:.2f}'.format(tempLow)
            #     self.ui.temperatureLowDisplay.display(temp4)
            #
            # if humidity > humHigh:
            #     humHigh = humidity
            #     hum3 = '{0:.2f}'.format(humHigh)
            #     self.ui.humidityHighDisplay.display(hum3)
            #
            # if humidity < humLow:
            #     humLow = humidity
            #     hum4 = '{0:.2f}'.format(humLow)
            #     self.ui.humidityLowDisplay.display(hum4)

            self.ui.temperatureHighDisplay.display(temp_max(len(temp_max)-1))
            self.ui.temperatureLowDisplay.display(temp_min(len(temp_min)-1))
            self.ui.humidityHighDisplay.display(hum_min(len(hum_min)-1))
            self.ui.humidityLowDisplay.display(hum_min(len(hum_min)-1))

            #array for last 10 values of humidity and temperature for graphical display
            if unit == 1:
                tempArr[samples]=temperature
                humArr[samples]=humidity
                samples = samples + 1
                y = [1,2,3,4,5,6,7,8,9,10]

                plt.subplot(2,1,1)
                plt.title('Temperature and Humidity Plot of last 10 Readings')
                plt.plot(y, tempArr,'.-')
                plt.ylabel('Degree Celcius')
                plt.legend()

                plt.subplot(2,1,2)
                plt.plot(y, humArr,'.-')
                plt.xlabel('Sample Number')
                plt.ylabel('Percent Humidity')
                plt.legend()
                plt.savefig('graph.jpg')

                if samples == 10:
                    samples=0

                #update the time of request for tem and humidity values
                newtime = time.strftime('%m-%d-%y  %H:%M:%S')
                self.ui.timeDisplay.setText(time_stamp[len(temp_value)-1])

                #update database
                crsr.execute("INSERT INTO dht_data values(?,?,?,?,?,?,?,?,?,?)",(newtime,temp1,tempUnit,temp2,temp3,temp4,hum1,hum2,hum3,hum4))
                connection.commit()

    def refresh(self):
        tempUnit = "°C"
        #conversion from cecius to fahrenheit
        cur_temp=temp_value[len(temp_value)-1]
        if unit == 0:
            # temperature = (temperature*1.8) + 32
            cur_temp = (temp_value[len(temp_value)-1]*1.8) + 32
            tempUnit = "°F"

        self.ui.temperatureDisplay.display(cur_temp)
        self.ui.humidityDisplay.display(hum_value[len(hum_value)-1])

        self.ui.temperatureAvgDisplay.display(temp_avg[len(temp_avg)-1])
        self.ui.humidityAvgDisplay.display(hum_avg[len(hum_avg)-1])
        self.ui.temperatureHighDisplay.display(temp_max[len(temp_max)-1])
        self.ui.temperatureLowDisplay.display(temp_min[len(temp_min)-1])
        self.ui.humidityHighDisplay.display(hum_max[len(hum_max)-1])
        self.ui.humidityLowDisplay.display(hum_min[len(hum_min)-1])

        #function to create a graph of last 10 temperature values
    def graphTempHum(self):
        global tempArr, humArr, temp_value,temp_avg,temp_min,temp_max,hum_value,hum_avg,hum_min,hum_max,time_stamp
        temp_value=list()
        temp_avg=list()
        temp_min=list()
        temp_max=list()

        hum_value=list()
        hum_avg=list()
        hum_min=list()
        hum_max=list()

        time_stamp=list()

        for i in range(3):
            while True:
                messages = sqs.receive_message(QueueUrl=test_queue_url,MaxNumberOfMessages=10) # adjust MaxNumberOfMessages if needed
                if 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
                    for message in messages['Messages']: # 'Messages' is a list
                        # process the messages
                        print(message['Body'])
                        packet=message['Body']
                        rec_msg=packet.split(',')
                        time_stamp.append(rec_msg[0])
                        temp_value.append(rec_msg[1])
                        temp_avg.append(rec_msg[2])
                        temp_min.append(rec_msg[3])
                        temp_max.append(rec_msg[4])
                        hum_value.append(rec_msg[5])
                        hum_avg.append(rec_msg[6])
                        hum_min.append(rec_msg[7])
                        hum_max.append(rec_msg[8])

                        # next, we delete the message from the queue so no one else will process it again
                        sqs.delete_message(QueueUrl=test_queue_url,ReceiptHandle=message['ReceiptHandle'])
                else:
                    print('Queue is now empty')
                    break

        samples=list(range(1,len(temp_value)+1))
        temp_value = list(map(float, temp_value))
        temp_avg = list(map(float, temp_avg))
        temp_min = list(map(float, temp_min))
        temp_max = list(map(float, temp_max))
        hum_value = list(map(float, hum_value))
        hum_avg = list(map(float, hum_avg))
        hum_min = list(map(float, hum_min))
        hum_max = list(map(float, hum_max))


        plt.subplot(2,1,1)
        plt.title('Temperature and Humidity Plot of last '+ str(len(samples))+' Readings'+' First Time-stamp: '
                  +time_stamp[0]+' Last Time-stamp: '+time_stamp[len(temp_value)-1])
##                  +' Samples retrieved: '+str(len(samples)))
        plt.plot(samples, temp_value, label='Temperature values')
        plt.plot(samples, temp_avg, label='Average Temperature')
        plt.plot(samples, temp_min, label='Minimum Temperature')
        plt.plot(samples, temp_max, label='Maximum Temperature')
        plt.ylabel('Degree Celcius')
        plt.xlabel('Sample number')
        plt.legend()

        plt.subplot(2,1,2)
        plt.plot(samples, hum_value, label='Humidity values')
        plt.plot(samples, hum_avg, label='Average Humidity')
        plt.plot(samples, hum_min, label='Minimum Humidity')
        plt.plot(samples, hum_max, label='Maximum Humidity')
        plt.ylabel('% Humidity')
        plt.xlabel('Sample number')
        plt.legend()
        plt.savefig('graph.jpg')
        plt.show()

        #function to switch from fahrenheit to celcius
    def celciusTemp(self):
        global unit, temp, tempAvg, tempHigh, tempLow, tempLimit
        if unit == 0:
            unit = 1
##            tempAvg = (temp_avg[len(temp_avg)-1]-32) * 0.5556
##            tempHigh = (temp_max[len(temp_max)-1]-32) * 0.5556
##            temp = '{0:.2f}'.format(tempHigh)
##            self.ui.temperatureHighDisplay.display(temp)
##            tempLow = (temp_min[len(temp_min)-1]-32) * 0.5556
##            temp = '{0:.2f}'.format(tempLow)
##            self.ui.temperatureLowDisplay.display(temp)
##            tempLimit = (tempLimit-32) * 0.5556
##            self.ui.tempThresholdDisplay.display(tempLimit);
##            temp_value[len(temp_value)-1] = (temp_value[len(temp_value)-1]-32) * 0.5556
##            self.ui.temperatureDisplay.display(temp_value[len(temp_value)-1])
        self.refresh()

        #function to switch from celcius to fahrenheit
    def fahrenheitTemp(self):
        global unit, temp, tempAvg, tempHigh, tempLow, tempLimit
        if unit == 1:
            unit = 0
            tempAvg = (temp_avg[len(temp_avg)-1]*1.8) + 32
            tempAvg = '{0:.2f}'.format(tempHigh)
            self.ui.temperatureAvgDisplay.display(tempAvg)
            tempHigh = (temp_max[len(temp_max)-1]*1.8) + 32
            temp = '{0:.2f}'.format(tempHigh)
            self.ui.temperatureHighDisplay.display(temp)
            tempLow = (temp_min[len(temp_min)-1]*1.8) + 32
            temp = '{0:.2f}'.format(tempLow)
            self.ui.temperatureLowDisplay.display(temp)
            tempLimit = (tempLimit*1.8) + 32
            temp = '{0:.2f}'.format(tempLimit)
            self.ui.tempThresholdDisplay.display(tempLimit);
            cur_temp= (temp_value[len(temp_value)-1]*1.8) + 32
            temp = '{0:.2f}'.format(cur_temp)
            self.ui.temperatureDisplay.display(temp)
##        self.refresh()

        #function to start and stop the timer to continuously update values
    def timerStartStop(self):
        global timerflag
        if timerflag == 0:
            self.ui.timerStatus.setStyleSheet("background-color: rgb(0, 255, 0);");
            self.timer.start()
            timerflag = 1
        elif timerflag == 1:
            self.ui.timerStatus.setStyleSheet("background-color: rgb(255, 0, 0);");
            self.timer.stop()
            timerflag = 0

        #function to set the high temperature threshold using dial
    def setTempLimit(self,value):
        global tempLimit, unit
        tempLimit = value
        if unit == 0:
            tempLimit = (tempLimit*1.8) + 32
        self.ui.tempThresholdDisplay.display(tempLimit);

        #function to set the high humidity threshold using dial
    def setHumLimit(self,value):
        global humLimit
        humLimit = value
        self.ui.humThresholdDisplay.display(humLimit);

        #function called when reset button is pressed to reset avg values
    def resetAvg(self):
        global tempAvg, tempHum, count
        tempAvg, tempHum, count = 0, 0, 0
        self.ui.temperatureAvgDisplay.display("")
        self.ui.humidityAvgDisplay.display("")

    def clearDB(self):
        global connection, crsr
        crsr.execute("DROP TABLE IF EXISTS dht_data")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
