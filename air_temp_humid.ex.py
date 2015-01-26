#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime
import MySQLdb as mdb

con = mdb.connect('mysql.oakwoodproduce.com', 'mike_op', 'flower15!', 'hydrolog');

sql_table = "sensor_readings"
sql_fields = "(reading_ts, sensor_location, sensor_type, sensor_value, create_user)"
sql_sensor_location = "bato" 
sql_sensor_type = "temp_air" 
sql_sensor_value = "0"
sql_create_user = "pi"
exec_count = 0
exec_status = "unsent"
sensor_status = "empty"
retry_count = 0

# Run the DHT program to get the humidity and temperature readings
while (sensor_status == "empty") :
	print "Get sensor reading..."
	output = subprocess.check_output(["/devroot/Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT", "22", "23"]);
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
print "Temperature: %.1f C" % temp
print "Temperature: %1f F" % tempF
  
  # search for humidity printout
matches = re.search("Hum =\s+([0-9.]+)", output)
if (not matches):
	print "Humidity reading not found. Exiting..."
	sys.exit()

humidity = float(matches.group(1))
  
print "Humidity:    %.1f %%" % humidity
 
# Append the data in the spreadsheet, including a timestamp
try:
	values = [datetime.datetime.now(), temp, humidity]
except:
	print "Unable to append data.  Check your connection?"
	sys.exit()

with con:
    cur = con.cursor()
    sql_sensor_type = "temp_air"
    # save as F temp
    sql_sensor_value = str(tempF) 
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES(current_timestamp,'" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)
    sqlExec = ""
    sql_sensor_type = "humidity" 
    sql_sensor_value = str(humidity)
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES(current_timestamp,'" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)
    sqlExec = ""
    
print "done"
