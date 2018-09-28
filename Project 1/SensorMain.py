import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import QDialog, QApplication

from SensorUI import Ui_SensorInterface

import Adafruit_DHT

import time

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_SensorInterface()
        self.ui.setupUi(self)
        
        global unit, count, tempAvg, humAvg
        unit = 1
        count,tempAvg,humAvg = 0,0,0

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.getTempHum)

        self.ui.refreshButton.clicked.connect(self.getTempHum)
        self.ui.celciusButton.clicked.connect(self.celciusTemp)
        self.ui.fahrenheitButton.clicked.connect(self.fahrenheitTemp)
        self.ui.timerStartButton.clicked.connect(self.timerStart)
        self.ui.timerStopButton.clicked.connect(self.timerStop)
        self.ui.resetButton.clicked.connect(self.resetAvg)
        
    def getTempHum(self):
        global unit, count, tempAvg, humAvg
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        threshold = 27

        if humidity is None and temperature is None:
            self.ui.alertDisplay.setText(" SENSOR DISCONNECTED")
            self.ui.temperatureDisplay.display("")
            self.ui.humidityDisplay.display("")
            self.ui.temperatureAvgDisplay.display("")
            self.ui.humidityAvgDisplay.display("")
        else:
            count = count + 1
            if unit == 0:
                temperature = (temperature*1.8) + 32
                threshold = 80.6
            temp = '{0:.2f}'.format(temperature)
            self.ui.temperatureDisplay.display(temp)
            hum = '{0:.2f}'.format(humidity)
            self.ui.humidityDisplay.display(hum)
            
            #Set an alert for high temperautre
            if temperature > threshold:
                self.ui.alertDisplay.setText("    HIGH TEMPERATURE")
            else:
                self.ui.alertDisplay.setText("")
    
            tempAvg=((tempAvg * (count-1)) + temperature) / count
            temp = '{0:.2f}'.format(tempAvg)
            self.ui.temperatureAvgDisplay.display(temp)
            humAvg=((humAvg * (count-1)) + humidity) / count
            hum = '{0:.2f}'.format(humAvg)
            self.ui.humidityAvgDisplay.display(hum)

        newtime = time.strftime('%m-%d-%y  %H:%M:%S')
        self.ui.timeDisplay.setText(newtime)

    def celciusTemp(self):
        global unit
        if unit == 0:
            unit = 1
        self.getTempHum()

    def fahrenheitTemp(self):
        global unit
        if unit == 1:
            unit = 0
        self.getTempHum()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()
        
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

