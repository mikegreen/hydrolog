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

# plot.ly settings, tokens created https://plot.ly/settings/api
import hydrologConfig

print hydrologConfig.plotly['username']

py.sign_in(hydrologConfig.plotly['username'], hydrologConfig.plotly['password'])
tokenPH 	= hydrologConfig.plotly['tokenPH']
tokenTempWater	= hydrologConfig.plotly['tokenTempWater']
tokenTempAir	= hydrologConfig.plotly['tokenTempAir']
tokenHumidity	= hydrologConfig.plotly['tokenHumidity']

address		= 0x4d
bus		= smbus.SMBus(1) 

print "start"

tracePH = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenPH,maxpoints=50),
	name="PH",
	yaxis="y",
	marker=dict(color='purple')
	)

traceTempWater = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenTempWater,maxpoints=50),
	name="Water Temp",
	yaxis="y2",
	marker=dict(color='blue')
	)
traceTempAir = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenTempAir,maxpoints=50),
	name="Air Temp",
	yaxis="y2",
	marker=dict(color='yellow')
	)
traceHumidity = Scatter(
	x=[],
	y=[],
	mode='lines+markers',
	stream=Stream(token=tokenHumidity,maxpoints=50),
	name="Humidity",
	yaxis="y2",
	marker=dict(color='orange')
	)


data = Data([tracePH, traceTempWater, traceTempAir, traceHumidity])

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
# this below creates the plot, and will overwrite if rerun. commented out for cron
# unique_url = py.plot(fig, filename = 'hydrolog testing 4')

streamPH = py.Stream(tokenPH)
streamPH.open()

streamTempWater = py.Stream(tokenTempWater)
streamTempWater.open()

streamTempAir = py.Stream(tokenTempAir)
streamTempAir.open()

streamHumidity = py.Stream(tokenHumidity)
streamHumidity.open()

def logPlot():
# water temp reading
	tempWater = ds18b20.readSensor()

# air temp+humid readings
	(tempAir, humidity) = dht22.readSensor()
	#tempAir  = ""
	#humidity = ""

# ph readings
	sample = phr.read()
	# print "     ph raw: " + str(sample)
	calced_ph = phr.calc_ph(sample)
	print "         ph: " + str(calced_ph)

	x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	y = calced_ph # calcPH

	streamPH.write(dict(x=x,y=y))
	#streamPHRaw.write(dict(x=x,y=sample))
	streamTempWater.write(dict(x=x,y=tempWater))
	streamTempAir.write(dict(x=x,y=tempAir))
	streamHumidity.write(dict(x=x,y=humidity))

logPlot()

