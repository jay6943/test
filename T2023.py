import cfg
import numpy as np
import matplotlib.pyplot as plt

def T202205():

  x = np.linspace(0, 2, 1001)

  d, f, y = 0.01, [], []
  for i in range(3):
    t = np.linspace(d-0.5, 0.5-d, 101) + i
    f.append(t)
    y.append(np.tan(t * np.pi))

  plt.plot([x[0], x[-1]], [0,0], '--')
  for i in range(3): plt.plot(f[i], y[i], 'k-')
  plt.plot(x, np.cos(x * np.pi), label=r'cos($\theta$)')
  plt.plot(x, np.cos((x + 0.5) * np.pi), label=r'cos($\pi$/2+$\theta$)')
  plt.xlabel(r'$\theta$')
  plt.xlim(0, 2)
  plt.ylim(-2, 2)
  xl = ['0','$\pi$/2','$\pi$','3$\pi$/2','2$\pi$']
  plt.xticks([0,0.5,1,1.5,2], xl)
  plt.grid(linestyle=':')
  plt.legend()
  plt.savefig(cfg.folder + 'T202205.png')

  return plt

def T202209():

  d, x, y = 0.01, [], []

  for i in range(7):
    t = (np.linspace(d-0.5, 0.5-d, 101) + i - 2)
    x.append(t)
    y.append(-np.tan(t * np.pi))

  for i in range(7): plt.plot(x[i], y[i], 'k-')
  plt.plot([1/2,1/2], [-4,4], '--')
  plt.xlabel('x', fontdict={'family':'serif'}, style='italic')
  plt.xlim(-1/2, 1/2)
  plt.ylim(-4, 4)
  xl = ['-$\pi$/2','-$\pi$/4','0','$\pi$/4','$\pi$/2']
  plt.xticks([(i * 0.5 - 1) for i in range(len(xl))], xl)
  plt.grid(linestyle=':')
  plt.savefig(cfg.folder + 'T202209.png')

  return plt

def T202216():

  d = 0.01
  x1 = np.linspace(d-2/3,12,101)
  x2 = np.linspace(d+2,12,101)
  f1 = np.log2(3 * x1 + 2)
  f2 = np.log2(x2 - 2) + 2

  plt.plot(x1, f1, label='f1')
  plt.plot(x2, f2, label='f2')
  plt.legend()
  plt.grid()
  plt.savefig(cfg.folder + 'T202216.png')

  return plt

def T202219():

  x = np.linspace(-2,4,1001)
  y = 2 * x**3 - 6 * x**2

  plt.plot(x, y)
  plt.xlim(-2,4)
  plt.ylim(-10,2)
  plt.grid()
  plt.savefig(cfg.folder + 'T202219.png')

  return plt

def T202221(arg, n):

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
  plt.savefig(cfg.folder + 'T202221-' + str(n) + '.png')

  return plt

if __name__ == '__main__':

  T202209().show()

  # for n in range(10): T202221(1, n).close()
