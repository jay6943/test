import time
import Arduino
import platform

if platform.system() == 'Windows':
  board = Arduino.Arduino('115200', port='COM5')
else:
  # sudo chmod 666 /dev/ttyACM0
  board = Arduino.Arduino('115200', port='/dev/ttyACM0')

board.pinMode(12, 'OUTPUT')

for _ in range(5):
  print('On')
  board.digitalWrite(12, 'HIGH')
  time.sleep(1)

  print('Off')
  board.digitalWrite(12, 'LOW')
  time.sleep(1)
