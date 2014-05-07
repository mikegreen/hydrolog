#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

print "DHT22 start"

sensor_status = "empty"
retry_count = 0

# Run the DHT program to get the humidity and temperature readings
while (sensor_status == "empty") :
	print "Get sensor reading..."
	output = subprocess.check_output(["/devroot/hydrolog/lib/Adafruit_DHT", "22", "23"]);
	print output
	matches = re.search("Temp =\s+([0-9.]+)", output)
	if (not matches):
		print "Temp reading not found. Retrying in 2 seconds..."
		print "Retry count: " + str(retry_count)
		retry_count = retry_count + 1
		time.sleep(2)
	else:
		sensor_status = "success"

temp = float(matches.group(1))
# conver to F
tempF = (temp *9/5)+32
print "Temperature: %1f F" % tempF
  
  # search for humidity printout
matches = re.search("Hum =\s+([0-9.]+)", output)
if (not matches):
	print "Humidity reading not found. Exiting..."
	sys.exit()

humidity = float(matches.group(1))
  
print "Humidity:    %.1f %%" % humidity
 
print "DHT22 finish"
