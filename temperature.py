import time
import serial

board = serial.Serial('COM5', 9600)
time.sleep(3)
print('Starting ...')

while True:
  print('Waitig ...')
  getval = board.write(b'$')
  time.sleep(1)
  print('Reading ...')
  val = board.readline()
  val = str(val, 'utf-8')
  print(val)
  time.sleep(1)
