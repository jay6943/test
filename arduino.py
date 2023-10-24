import platform
import pyfirmata

if platform.system() == 'Windows':
  board = pyfirmata.Arduino('COM5')
else:
  # sudo chmod 666 /dev/ttyACM0
  board = pyfirmata.Arduino('/dev/ttyACM0')

while True:
  val = input('입력: 0/1/2?')

  if val == '0':
    board.digital[13].write(0)

  elif val == '1':
    board.digital[13].write(1)

  elif val == '2':
    board.digital[13].write(0)
    break
