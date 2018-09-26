import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QApplication

from SensorUI import Ui_Form

import Adafruit_DHT

import time

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()


    def getTempHum(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4))

        if humidity is None and temperature is None:
            self.alertDisplay.setText("Sensor Disconnected")
            Self.temperatureDisplay.setText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window  = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

