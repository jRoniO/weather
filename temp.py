#!/usr/bin/python

import time

from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
        temperature = str(sensor.get_temperature())
        avrundning = temperature[0:4]
        file1 = open("/var/www/html/tempData.txt","w")
        file1.write('\nTemperaturen är: %s grader celsius' % avrundning)
        file1.close()

        #print('The temperature is %s celsius' % avrundning)
