import numpy as np
import matplotlib.pyplot as plt

folder = '..//data/'

xl0 = ['0', '$\pi$/2', '$\pi$', '3$\pi$/2', '2$\pi$', '5$\pi$/2']
xl1 = ['-5$\pi$/2', '-2$\pi$', '-3$\pi$/2', '-$\pi$', '-$\pi$/2'] + xl0
xl2 = xl1.copy()
xl3 = ['-9$\pi$/4', '-7$\pi$/4', '-5$\pi$/4', '-3$\pi$/4', '-$\pi$/4']
xl4 = xl3 + ['$\pi$/4', '3$\pi$/4', '5$\pi$/4', '7$\pi$/4', '9$\pi$/4']

for i in range(len(xl4)): xl2.insert(i*2+1, xl4[i])

def T22_5():

  x = np.linspace(0, 2, 1001)

  d, f, y = 0.01, [], []
  for i in range(3):
    t = np.linspace(d-0.5, 0.5-d, 101) + i
    f.append(t)
    y.append(np.tan(t * np.pi))

  fig, ax = plt.subplots(1)
  ax.plot([x[0], x[-1]], [0,0], '--')
  for i in range(3): ax.plot(f[i], y[i], 'k-')
  ax.plot(x, np.cos(x * np.pi), label=r'cos($\theta$)')
  ax.plot(x, np.cos((x + 0.5) * np.pi), label=r'cos($\pi$/2+$\theta$)')
  ax.set_xlabel(r'$\theta$')
  ax.set(xlim=(0, 2), ylim=(-2, 2))
  ax.set_xticks([0, 0.5, 1, 1.5, 2])
  # ax.set_xticklabels(xl0)
  ax.grid(linestyle=':')
  plt.legend()
  plt.savefig(folder + 'T22_5.png')

  return plt

def T22_9(period):

  d, x, y = 0.01, [], []

  for i in range(7):
    t = (np.linspace(d-0.5, 0.5-d, 101) + i - 2) / period
    x.append(t)
    y.append(-np.tan(period * t * np.pi))

  fig, ax = plt.subplots(1)
  for i in range(7): ax.plot(x[i], y[i], 'k-')
  ax.plot([1/2,1/2], [-4,4], '--')
  ax.set_xlabel('x', fontdict={'family':'serif'}, style='italic')
  ax.set(xlim=(-1/2, 1/2), ylim=(-4, 4))
  xl = xl2[xl2.index('-$\pi$/2'):xl2.index('$\pi$/2')+1]
  ax.set_xticks([(i * 0.5 - 1)/period for i in range(len(xl))])
  ax.set_xticklabels(xl)
  ax.grid(linestyle=':')
  plt.savefig(folder + 'T22_9.png')

  return plt

def T22_16():

  d = 0.01
  x1 = np.linspace(d-2/3,12,101)
  x2 = np.linspace(d+2,12,101)
  f1 = np.log2(3 * x1 + 2)
  f2 = np.log2(x2 - 2) + 2

  plt.plot(x1, f1, label='f1')
  plt.plot(x2, f2, label='f2')
  plt.legend()
  plt.grid()
  plt.savefig(folder + 'T22_16.png')

  return plt

def T22_19():

  x = np.linspace(-2,4,1001)
  y = 2 * x**3 - 6 * x**2

  plt.plot(x, y)
  plt.xlim(-2,4)
  plt.ylim(-10,2)
  plt.grid()
  plt.savefig(folder + 'T22_16.png')

  return plt

def T22_21(arg, n):

  xmin, xmax = -4, 10

  x1 = np.linspace(xmin,0,1001)
  x2 = np.linspace(0,xmax,1001)

  y1 = 3 ** (x1 + 2) - n
  y2 = np.log2(x2 + 4) - n

  plt.figure(dpi=120)
  if arg:
    plt.title('n = %d' % n)
    plt.plot(x1, np.abs(y1), linewidth=1)
    plt.plot(x2, np.abs(y2), linewidth=1)
    plt.ylim([-2, 10])
  else:
    plt.plot(x1, y1)
    plt.plot(x2, y2)
  plt.xlim([xmin,xmax])
  plt.grid()
  plt.savefig(folder + 'T22_21_' + str(n) + '.png')

  return plt

def S230411():

  a = np.linspace(0,1,361) * 2 * np.pi
  x = np.cos(a)
  y = np.sin(a)
  l = 1.2

  _, ax = plt.subplots(1, figsize=(10,10))

  ax.plot(x,y)
  ax.plot([0,np.cos(a[180-45])], [0,np.sin(a[180-45])])
  ax.set_aspect('equal')
  ax.set(xlim=(-l,l),ylim=(-l,l))
  ax.set_xticks([-1,0,1])
  ax.set_yticks([-1,0,1])
  ax.grid()

  plt.savefig(folder + 'S230411.png')

  return plt

if __name__ == '__main__':

  T22_5().show()

  # for n in range(10): T22_21(1, n).close()
