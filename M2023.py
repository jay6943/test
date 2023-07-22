import cfg
import numpy as np
import matplotlib.pyplot as plt

def M230411():

  a = np.linspace(0,1,361) * 2 * np.pi
  x = np.cos(a)
  y = np.sin(a)
  l = 1.2

  a1 = 180-45
  x1 = np.cos(a[a1])
  y1 = np.sin(a[a1])

  plt.figure(figsize=(10,10))
  plt.plot(x,y)
  plt.plot([0,x1], [0,y1])
  plt.plot([0,x1], [0,0])
  plt.plot([x1,x1], [0,y1])
  plt.xlim(-l,l)
  plt.ylim(-l,l)
  plt.xticks([-1,0,1])
  plt.yticks([-1,0,1])
  plt.grid()
  plt.savefig(cfg.folder + 'M230411.png')

  return plt

def M220909():

  x = np.linspace(0,12,361)
  f = np.cos(x * np.pi / 6)
  g = -3 * f - 1
  k = 1 / 2

  plt.plot(x,f)
  plt.plot(x,g)
  plt.plot([0,12],[k,k], '--')
  plt.xlim(x[0],x[-1])
  plt.grid()
  plt.savefig(cfg.folder + 'M220909.png')

  return plt

def M220607():

  x = np.linspace(0,1,361)
  f = -np.sin(2 * x * np.pi)

  plt.plot(x,f)
  plt.plot([0.25,0.75,],[-1,1])
  xl = ['0','$\pi$/4','$\pi$/2','3$\pi$/4','$\pi$']
  plt.xticks([0,0.25,0.5,0.75,1], xl)
  plt.xlim(x[0],x[-1])
  plt.grid()
  plt.savefig(cfg.folder + 'M220607.png')

  return plt

if __name__ == '__main__':

  M230411().show()