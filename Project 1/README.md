   # Project 1 : Local QT-based UI
   
   ### Created By: Preshit Harlikar
  
  
   #### This project demonstrates development of a rapid prototype of a stand-alone temperature monitoring device with a local user interface. The temperature and humidity sensor used is DHT22 which is interfaced with Raspberry Pi. A User Interface is created for the temperature and humidity sensor using PyQT.
   
   ## Installation Guide
   #### To run this project on Raspeberry Pi, you need to install Qt and PyQt using,
         sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
         sudo apt-get install qttools5-dev-tools
   
   #### Some packages have to be installed
         sudo apt-get update
         sudo apt-get install build-essential python-dev python-openssl git
   
   #### Now clone the pre-built Adafruit library for DHT22
         git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
         sudo python3 setup.py install
   
   #### Clone this repository and run the program
         git clone https://github.com/hpreshit/eid-fall2018 && cd Project\ 1/
         python3 SensorMain.py
      
   #### After you run the Python file, you will get a UI like this:
   [GitHub Logo](SensorUI.JPG)
   
