#!/usr/bin/python3
#!/usr/bin/env python3


import serial
import time

from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
	temperature = str(sensor.get_temperature())
	avrundning = temperature[0:4]
	line = ser.readline().decode('utf-8').rstrip()
	if line:
		remove_negative = line.replace('-','0,00')
		remove_decimal = remove_negative[0:4]
		print(f'\rTemperaturen är %s grader celsius och vindhastigheten är %s m/s' % (avrundning, remove_decimal), end='')
		time.sleep(0.5)

	else:
		print(f'\rTemperaturen är %s grader celsius och vindhastigheten är %s m/s' % (avrundning, line), end='')
		time.sleep(1)


