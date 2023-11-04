import serial
import time

ser = serial.Serial('COM5', 9600)

while True:
  if ser.readable():
    val = input()

    if val == '1':
      val = val.encode('utf-8')
      ser.write(val)
      print("LED TURNED ON")
      time.sleep(1)

    elif val == '0':
      val = val.encode('utf-8')
      ser.write(val)
      print("LED TURNED OFF")
      time.sleep(1)

    elif val == '2':
      val = '0'
      val = val.encode('utf-8')
      ser.write(val)
      ser.close()
      break
