import time
import platform
import pyfirmata

if platform.system() == 'Windows':
  board = pyfirmata.Arduino('COM5')
else:
  # sudo chmod 666 /dev/ttyACM0
  board = pyfirmata.Arduino('/dev/ttyACM0')

for _ in range(5):
  print('On')
  board.digital[12].write(1)
  time.sleep(1)

  print('Off')
  board.digital[12].write(0)
  time.sleep(1)
