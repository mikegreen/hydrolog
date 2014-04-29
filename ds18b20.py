import os
import glob
import time

print "ds18b20 start"

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

tempC = 0.00
tempF = 0.00

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

print('ds18b20 temperature:')
print(read_temp())
	
#while True:
#	print(read_temp())	
#	time.sleep(1)

print "ds18b20 finish"