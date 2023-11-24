import keyboard
import time

def loop_exit():
  try:
    while 1:
      for j in range(3):
        print(j)
        time.sleep(1)
      print('done.')
  except KeyboardInterrupt:
    print('stop.')


def loop_esc():
  running = 1
  while running:
    for j in range(3):
      print(j)
      time.sleep(0.5)

    for i in range(30):
      if keyboard.is_pressed('esc'):
        running = 0
        break
      print('-', end=' ')
      time.sleep(0.1)
    print('\b' * 100, end='')


if __name__ == '__main__': loop_esc()
