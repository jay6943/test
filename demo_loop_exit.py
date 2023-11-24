import keyboard
import time

j = 0

while 1:
  if keyboard.is_pressed('esc'):
    print('You pressed esc')
    break
  print(j)
  j += 1
  time.sleep(0.5)
