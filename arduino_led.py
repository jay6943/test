import time
import Arduino
import platform

pinNum = 12

if platform.system() == 'Windows':
  board = Arduino.Arduino('9600', port='COM5')
else:
  # sudo chmod 666 /dev/ttyACM0
  board = Arduino.Arduino('9600', port='/dev/ttyACM0')

board.pinMode(pinNum, 'OUTPUT')

for _ in range(2):
  print('On')
  board.digitalWrite(pinNum, 'HIGH')
  time.sleep(1)

  print('Off')
  board.digitalWrite(pinNum, 'LOW')
  time.sleep(1)

board.close()
