#!/usr/bin/python3

import serial
import time

if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
        ser.flush()

while True:
        if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                file = open("/var/www/html/vindData.txt","w")
                file.write('Vindhastigheten är: %s m/s' % line)
                file.close()
