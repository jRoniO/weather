#!/usr/bin/python3
#!/usr/bin/env python3

import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)#!/usr/bin/env python3
'''
import time
import serial

windPrint = ""
while 1:
        ser = serial.Serial('/dev/ttyACM0', 9600)
print(f'\rVindhastigheten är: {windPrint}', end='')
time.sleep(1)
'''
