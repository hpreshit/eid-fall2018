   # Project 1 : Local QT-based UI
   
   ### Created By: Preshit Harlikar
  
  ![GitHub Logo](SensorUI.JPG)
  
   #### This project demonstrates development of a rapid prototype of a stand-alone temperature monitoring device with a local user interface. The temperature and humidity sensor used is DHT22 which is interfaced with Raspberry Pi. A User Interface is created for the temperature and humidity sensor using PyQT.
   
   ## Installation Guide
   ### To run this project on Raspeberry Pi, you need to install Qt and PyQt using,
         sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
         sudo apt-get install qttools5-dev-tools
   
   ### Some packages have to be installed
         sudo apt-get update
         sudo apt-get install build-essential python-dev python-openssl git
   
   ### Now clone the pre-built Adafruit library for DHT22
         git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
         sudo python3 setup.py install
   
   ### Clone this repository and run the program
         git clone https://github.com/hpreshit/eid-fall2018 && cd Project\ 1/
         python3 SensorMain.py
 
   
   ## Project Work
   ### The DHT22 temperature and humidity sensor is interfaced with the Raspberry Pi and an Interactive GUI is created to display the Temperature and Humidity values. The GUI has the basic functionalities like:
   #### 1. Requesting current values from of the temperature and humidity from the DHT22
   #### 2. Display the values of temperature and humidity as well as the time of request
   #### 3. Generate an error message if the sensor is inactive or disconnected
  
   ## Project Additions
   ### The additional features added to the project are:
   #### 1. Retrieve temperature and humidity values using a timer
   #### 2. Continuously calculate and display the average temperature & humidity values
   #### 3. Switch between Celcius and Fahrenheit units of temperature
   #### 4. Allow user to set an alarm for an input high temperature and humidity value using a dial
   #### 5. Display graph of last 10 values of temperature and humidity values
   
