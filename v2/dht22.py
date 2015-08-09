#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 23

print "DHT22 start"

def readSensor():
	sensor_status = "empty"
	retry_count = 0
	# Run the DHT program to get the humidity and temperature readings
	while (sensor_status == "empty") :
#	        print "Get sensor reading..."
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		if humidity is not None and temperature is not None:
#		        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
			sensor_status = "success"
		else:
	                print "Temp reading not found. Retrying in 2 seconds..retry count: " + str(retry_count)
	                retry_count = retry_count + 1
	                time.sleep(2)
	
	# convert to F and round
	tempF = "{0:0.2f}".format((temperature *9/5)+32)
	print "Temperature: " + str(tempF)
	# tempF = "{0:0.2f}".format(tempF)
	humidity = "{0:0.2f}".format(humidity)
	print "   Humidity: " + str(humidity)
#	return tempF
	
# print "DHT22 finish"
