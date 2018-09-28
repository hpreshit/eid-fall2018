import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import QDialog, QApplication

from SensorUI import Ui_Form

import Adafruit_DHT

import time

class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.refreshButton.clicked.connect(self.getTempHum)
        self.ui.celciusButton.clicked.connect(self.celciusTemp)
        self.ui.fahrenheitButton.clicked.connect(self.fahrenheitTemp)
        global unit
        unit = 1

    def getTempHum(self):
        global unit
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

        if humidity is None and temperature is None:
            self.ui.alertDisplay.setText(" SENSOR DISCONNECTED")
            self.ui.temperatureDisplay.display("")
            self.ui.humidityDisplay.display("")
        else:
            if unit == 0:
                temperature = (temperature*1.8) + 32
            temp = '{0:.2f}'.format(temperature)
            self.ui.temperatureDisplay.display(temp)
            hum = '{0:.2f}'.format(humidity)
            self.ui.humidityDisplay.display(hum)
            #Set an alert for high temperautre
            if temperature > 26:
                self.ui.alertDisplay.setText("    HIGH TEMPERATURE")
            else:
                self.ui.alertDisplay.setText("")

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())

