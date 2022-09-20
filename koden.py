#!/usr/bin/python

import time

from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
	temperature = str(sensor.get_temperature())
	avrundning = temperature[0:4]
	print("The temperature is %s celsius" % avrundning)
	time.sleep(1)
