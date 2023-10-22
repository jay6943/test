import time
import platform
import pyfirmata

if platform.system() == 'Windows':
  board = pyfirmata.Arduino('COM5')
else:
  # sudo chmod 666 /dev/ttyACM0
  board = pyfirmata.Arduino('/dev/ttyACM0')

while True:
  board.digital[13].write(1)
  time.sleep(1)

  board.digital[13].write(0)
  time.sleep(1)
