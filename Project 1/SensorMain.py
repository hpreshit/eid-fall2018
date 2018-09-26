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

    def getTempHum(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

        if humidity is None and temperature is None:
            self.ui.alertDisplay.setText("Sensor Disconnected")
            self.ui.temperatureDisplay.setText("")
            self.ui.humidityDisplay.setText("")
        else:
            temp = '{0:.2f}'.format(temperature)
            self.ui.temperatureDisplay.setText(temp)
            hum = '{0:.2f}'.format(humidity)
            self.ui.humidityDisplay.setText(hum)
            #Set an alert for high temperautre
            if temperature > 26:
                self.ui.alertDisplay.setText("HIGH TEMPERATURE")
            else:
                self.ui.alertDisplay.setText("")

        newtime = time.strftime('%m-%d-%y  %H:%M:%S')
        self.ui.timeDisplay.setText(newtime)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())

