import os
import glob
import time
import sys

print "ds18b20 start"

# for rpi - need below line in config.txt
# dtoverlay=w1-gpio

# loading these in /etc/modules now
# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
probe_dir = '28-0000068a9c8a'

print "base_dir:",base_dir
print "does base_dir exist? ", os.path.isdir(base_dir)

probe_dir_full = os.path.join(base_dir,probe_dir)
print "device_folder: " + probe_dir_full

print "does device_folder exist? ",os.path.isdir(probe_dir_full)

if os.path.isdir(probe_dir_full):
	#device_folder = glob.glob(probe_dir_full)[0]
	device_file = probe_dir_full + '/w1_slave'
	print "therm found: ", probe_dir_full
	sensor_present = True
else:
	sensor_present = False
	print "therm not found"

tempC = 0.00
tempF = 0.00

def readSensor():
	read_temp_raw()
	read_temp()
	print " water temp: " + str(tempF)	
	return tempF

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        global tempC
	global tempF
	tempC = float(temp_string) / 1000.0
        tempF = round(tempC * 9.0 / 5.0 + 32.0,2)
        return tempC, tempF

if sensor_present:
	print('ds18b20 temperature:')
	print(read_temp())
else:
	print "nothing to do, sensor not found"

print "ds18b20 finish"

