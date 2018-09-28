# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SensorUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 550)
        font = QtGui.QFont()
        font.setFamily("PibotoLt")
        Form.setFont(font)
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(10, 500, 121, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(520, 500, 121, 41))
        self.exitButton.setAutoDefault(False)
        self.exitButton.setObjectName("exitButton")
        self.temperatureLabel = QtWidgets.QLabel(Form)
        self.temperatureLabel.setGeometry(QtCore.QRect(90, 70, 91, 91))
        self.temperatureLabel.setText("")
        self.temperatureLabel.setPixmap(QtGui.QPixmap("../../../Downloads/rsz_2temperature.png"))
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.humidityLabel = QtWidgets.QLabel(Form)
        self.humidityLabel.setGeometry(QtCore.QRect(485, 80, 81, 81))
        self.humidityLabel.setText("")
        self.humidityLabel.setPixmap(QtGui.QPixmap("../../../Downloads/rsz_1humidity.png"))
        self.humidityLabel.setObjectName("humidityLabel")
        self.timeLabel = QtWidgets.QLabel(Form)
        self.timeLabel.setGeometry(QtCore.QRect(290, 10, 81, 71))
        self.timeLabel.setText("")
        self.timeLabel.setPixmap(QtGui.QPixmap("../../../Downloads/rsz_1rsz_clock (1).png"))
        self.timeLabel.setObjectName("timeLabel")
        self.timeDisplay = QtWidgets.QLineEdit(Form)
        self.timeDisplay.setGeometry(QtCore.QRect(250, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.timeDisplay.setFont(font)
        self.timeDisplay.setObjectName("timeDisplay")
        self.alertDisplay = QtWidgets.QLineEdit(Form)
        self.alertDisplay.setGeometry(QtCore.QRect(200, 260, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.alertDisplay.setFont(font)
        self.alertDisplay.setAutoFillBackground(False)
        self.alertDisplay.setObjectName("alertDisplay")
        self.alertLabel = QtWidgets.QLabel(Form)
        self.alertLabel.setGeometry(QtCore.QRect(285, 180, 91, 81))
        self.alertLabel.setText("")
        self.alertLabel.setPixmap(QtGui.QPixmap("../../../Downloads/rsz_alert.png"))
        self.alertLabel.setObjectName("alertLabel")
        self.temperatureDisplay = QtWidgets.QLCDNumber(Form)
        self.temperatureDisplay.setGeometry(QtCore.QRect(60, 170, 151, 61))
        self.temperatureDisplay.setObjectName("temperatureDisplay")
        self.humidityDisplay = QtWidgets.QLCDNumber(Form)
        self.humidityDisplay.setGeometry(QtCore.QRect(450, 170, 151, 61))
        self.humidityDisplay.setObjectName("humidityDisplay")
        self.celciusButton = QtWidgets.QPushButton(Form)
        self.celciusButton.setGeometry(QtCore.QRect(30, 170, 31, 31))
        self.celciusButton.setObjectName("celciusButton")
        self.fahrenheitButton = QtWidgets.QPushButton(Form)
        self.fahrenheitButton.setGeometry(QtCore.QRect(30, 200, 31, 31))
        self.fahrenheitButton.setObjectName("fahrenheitButton")
        self.timerStartButton = QtWidgets.QPushButton(Form)
        self.timerStartButton.setGeometry(QtCore.QRect(180, 500, 121, 41))
        self.timerStartButton.setObjectName("timerStartButton")
        self.timerStopButton = QtWidgets.QPushButton(Form)
        self.timerStopButton.setGeometry(QtCore.QRect(350, 500, 121, 41))
        self.timerStopButton.setObjectName("timerStopButton")

        self.retranslateUi(Form)
        self.exitButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.refreshButton.setText(_translate("Form", "Refresh"))
        self.exitButton.setText(_translate("Form", "Exit"))
        self.celciusButton.setText(_translate("Form", "C"))
        self.fahrenheitButton.setText(_translate("Form", "F"))
        self.timerStartButton.setText(_translate("Form", "Start Timer"))
        self.timerStopButton.setText(_translate("Form", "Stop Timer"))

