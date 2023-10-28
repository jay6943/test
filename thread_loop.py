import threading

def job1():
  while 1:
    print('first')

def job2():
  while 1:
    print('second')

work1 = threading.Thread(target=job1)
work2 = threading.Thread(target=job2)

work1.start()
work2.start()
