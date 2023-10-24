import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
  val = input('입력: 0/1/2?')

  if val == '0':
    ser.write(b'L')
    print("LED TURNED OFF")

  elif val == '1':
    ser.write(b'H')
    print("LED TURNED ONN")

  elif val == '2':
    ser.write(b'L')
    break

ser.close()
