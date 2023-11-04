import time
import serial

ser = serial.Serial('COM5', 9600)
time.sleep(3)
print('Starting ...')
ser.write(b'H')
time.sleep(1)
ser.close()
