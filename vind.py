#!/usr/bin/python3
#!/usr/bin/env python3

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
	line = ser.readline().decode('utf-8').rstrip()
	
	if line:
		remove_negative = line.replace('-','0,00')
		remove_decimal = remove_negative[0:4]
		print(f'Vindhastigheten är %s m/s' % remove_decimal)
		time.sleep(1)

	else:
		print(f'Vindhastigheten är %s m/s' % line)
		time.sleep(1)
		
