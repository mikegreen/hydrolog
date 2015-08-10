#!/usr/bin/python

import sys
import ssl
import re
import subprocess 
import smbus 
import datetime
import time 
import plotly.plotly as py
from plotly.graph_objs import *

# import ph stuff
import pHReader

phr = pHReader.pHReader()

# import sensor stuff
import dht22
import ds18b20
#import gpioWaterLevel

py.sign_in('username', 'password')
tokenPH = "xxxxx"
tokenPHRaw = "xxxxx"

address = 0x4d
bus = smbus.SMBus(1) 

print "start"

tracePH = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenPH,maxpoints=500),
	name="PH",
	yaxis="y"
	)

tracePHRaw = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenPHRaw,maxpoints=500),
	name="sensor value",
	yaxis="y2"
	)

data = Data([tracePH, tracePHRaw])

layout = Layout(
	# title="hydrolog test 1",
	yaxis=YAxis(
		title="PH",
		side="left",
		range=[5.5,9.5]
		# autorange="true"
		),
	yaxis2=YAxis(
		title="sensor value",
		side="right",
		overlaying="y",
		autorange="true"
		)
	)

fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename = 'ph test 16')

streamPH = py.Stream(tokenPH)
streamPH.open()

streamPHRaw = py.Stream(tokenPHRaw)
streamPHRaw.open()

print "Start while looping"

while (1 == 1):
# water temp reading
	ds18b20.readSensor()

# air temp+humid readings
	dht22.readSensor()

# ph readings
	sample = phr.read()
	print "     ph raw: " + str(sample)
	calced_ph = phr.calc_ph(sample)
	print "         ph: " + str(calced_ph)

	x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	y = calced_ph # calcPH

	streamPH.write(dict(x=x,y=y))
	streamPHRaw.write(dict(x=x,y=sample))

	time.sleep(2)

