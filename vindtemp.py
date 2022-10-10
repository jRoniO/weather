#!/usr/bin/python3

import serial
import time
from w1thermsensor import W1ThermSensor
import threading

sensor = W1ThermSensor()

if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
        ser.flush()

def print_wind_speed():
        while True:
                try:
                        if ser.in_waiting > 0:
                                line = ser.readline().decode('utf-8').rstrip()
                                file = open("/var/www/html/vindData.txt","w")
                                file.write('Vindhastigheten är: %s m/s' % line)
                                file.close()
                except UnicodeDecodeError:
                        ser.readline().decode('utf-8').rstrip()
        return

def print_temperature():
        while True:
                temperature = str(sensor.get_temperature())
                avrundning = temperature[0:4]
                file1 = open("/var/www/html/tempData.txt","w")
                file1.write('Temperaturen är %s grader celsius' % avrundning)
                file1.close()
        return

t1 = threading.Thread(target = print_wind_speed)
t2 = threading.Thread(target = print_temperature)

t1.start()
t2.start()


t1.join()
t2.join()
