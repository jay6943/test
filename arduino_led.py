import time
import Arduino
import platform

if platform.system() == 'Windows':
  board = Arduino.Arduino('115200', port='COM5')
else:
  board = Arduino.Arduino('115200', port='/dev/ttyACM0')

board.pinMode(13, 'OUTPUT')

while True:
  print('On')
  board.digitalWrite(13, 'HIGH')
  time.sleep(1)

  print('Off')
  board.digitalWrite(13, 'LOW')
  time.sleep(1)
