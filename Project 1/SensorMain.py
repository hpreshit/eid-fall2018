import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import QDialog, QApplication

from SensorUI import Ui_SensorInterface

import matplotlib.pyplot as plt

import Adafruit_DHT

import time

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        #integrating the UI
        self.ui = Ui_SensorInterface()      
        self.ui.setupUi(self)
        
        #global variables
        global unit, count, tempAvg, humAvg, samples, tempArr, humArr, timerflag, tempLimit, humLimit 
        unit = 1
        count,tempAvg,humAvg,samples,timerflag = 0,0,0,0,0
        tempArr = [None]*10  
        humArr = [None]*10 
        tempLimit = 100
        humLimit = 100
        
        #initializing timer
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.getTempHum)

        self.ui.refreshButton.clicked.connect(self.getTempHum)
        self.ui.celciusButton.clicked.connect(self.celciusTemp)
        self.ui.fahrenheitButton.clicked.connect(self.fahrenheitTemp)
        self.ui.timerButton.clicked.connect(self.timerStartStop)
        self.ui.resetButton.clicked.connect(self.resetAvg)
        self.ui.graphTempButton.clicked.connect(self.graphTemp)
        self.ui.graphHumButton.clicked.connect(self.graphHum)
        self.ui.tempDial.valueChanged.connect(self.setTempLimit)
        self.ui.humDial.valueChanged.connect(self.setHumLimit)
        
        #function to get temp and humidity from the sensor
    def getTempHum(self):
        global unit, count, tempAvg, humAvg, tempArr, humArr, samples, tempLimit, humLimit
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

        #check if sensor is disconnected
        if humidity is None and temperature is None:
            self.ui.alertDisplay.setText(" SENSOR DISCONNECTED")
            self.ui.temperatureDisplay.display("")
            self.ui.humidityDisplay.display("")
            self.ui.temperatureAvgDisplay.display("")
            self.ui.humidityAvgDisplay.display("")
            self.ui.sensorStatus.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.ui.sensorStatus.setStyleSheet("background-color: rgb(0, 255, 0);")
            count = count + 1
            
            #conversion from cecius to fahrenheit
            if unit == 0:
                temperature = (temperature*1.8) + 32
                threshold = 80.6    
            
            #display current temp and humidity value on LCD Display
            temp = '{0:.2f}'.format(temperature)
            self.ui.temperatureDisplay.display(temp)
            hum = '{0:.2f}'.format(humidity)
            self.ui.humidityDisplay.display(hum)
            
            #Set an alert for high temperautre
            if temperature > tempLimit:
                self.ui.alertDisplay.setText("    HIGH TEMPERATURE")
            elif humidity > humLimit:
                self.ui.alertDisplay.setText("        HIGH HUMIDITY")
            else:
                self.ui.alertDisplay.setText("")
                
            #calculating average temperature and humidity continuously for each sample    
            tempAvg=((tempAvg * (count-1)) + temperature) / count
            temp = '{0:.2f}'.format(tempAvg)
            self.ui.temperatureAvgDisplay.display(temp)
            humAvg=((humAvg * (count-1)) + humidity) / count
            hum = '{0:.2f}'.format(humAvg)
            self.ui.humidityAvgDisplay.display(hum)
            
            #array for last 10 values of humidity and temperature for graphical display
            if unit == 1:
                tempArr[samples]=temperature
                humArr[samples]=humidity
                samples = samples + 1
                if samples == 10:
                    samples=0

        #update the time of request for tem and humidity values            
        newtime = time.strftime('%m-%d-%y  %H:%M:%S')
        self.ui.timeDisplay.setText(newtime)

        #function to create a graph of last 10 temperature values
    def graphTemp(self):
        global tempArr
        y = [1,2,3,4,5,6,7,8,9,10]
        
        plt.plot(y, tempArr, label='Temperature')
        
        plt.xlabel('Sample Number')
        plt.ylabel('Degree Celcius')
        plt.title('Temperature Plot of last 10 Readings')
        plt.legend()
        plt.show()
        
        #function to create a graph of last 10 humidity values
    def graphHum(self):
        global humArr
        y = [1,2,3,4,5,6,7,8,9,10]
        
        plt.plot(y, humArr, label='Humidity')
        
        plt.xlabel('Sample Number')
        plt.ylabel('Percent Humidity')
        plt.title('Humidity Plot of last 10 Readings')
        plt.legend()
        plt.show()
        
        #function to switch from fahrenheit to celcius
    def celciusTemp(self):
        global unit, tempAvg
        if unit == 0:
            unit = 1
            tempAvg = (tempAvg-32) * 0.5556
        self.getTempHum()

        #function to switch from celcius to fahrenheit
    def fahrenheitTemp(self):
        global unit, tempAvg
        if unit == 1:
            unit = 0
            tempAvg = (tempAvg*1.8) + 32
        self.getTempHum()      

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())

