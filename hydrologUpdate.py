#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

print "Starting updateHydrolog.py @",time.strftime("%Y-%m-%d %H:%M:%S"),"GMT"

import dbCreds
import dht22
import ds18b20
import gpioWaterLevel

# moved to other file
# con = mdb.connect('serverURL', 'username', 'password', 'dbName');

sql_table = "sensor_readings"
sql_fields = "(reading_ts, sensor_location, sensor_type, sensor_value, create_user)"
sql_sensor_location = "bato" 
sql_sensor_type = "temp_air" 
sql_sensor_value = "0"
sql_create_user = "pi"
exec_count = 0
sql_insert_time = time.strftime('%Y-%m-%d %H:%M:%S')


with dbCreds.con:
    cur = dbCreds.con.cursor()
    # insert air temp
    sql_sensor_type = "temp_air"
    # save as F temp
    sql_sensor_value = str(dht22.tempF) 
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES('" + sql_insert_time + "','" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)
    # insert humidity 
    sqlExec = ""
    sql_sensor_type = "humidity" 
    sql_sensor_value = str(dht22.humidity)
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES('" + sql_insert_time + "','" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)
    #insert water temp
    sqlExec = ""
    sql_sensor_type = "temp_water" 
    sql_sensor_value = str(ds18b20.tempF)
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES('" + sql_insert_time + "','" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)
    #insert water level
    sqlExec = ""
    sql_sensor_type = "water_level" 
    sql_sensor_value = str(gpioWaterLevel.waterSensor)
    sqlExec = "INSERT INTO " + sql_table + sql_fields + "VALUES('" + sql_insert_time + "','" + sql_sensor_location + "','" + sql_sensor_type + "','" + sql_sensor_value + "','" + sql_create_user + "')" 
    print sqlExec
    cur.execute(sqlExec)


