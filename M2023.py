import numpy as np
import matplotlib.pyplot as plt

folder = '..//data/'

def M220909():

  x = np.linspace(0,12,361)
  f = np.cos(x * np.pi / 6)
  g = -3 * f - 1
  k = 1 / 2

  _, ax = plt.subplots(1)

  ax.plot(x,f)
  ax.plot(x,g)
  ax.plot([0,12],[k,k], '--')
  ax.grid()

  plt.savefig(folder + 'M220909.png')

  return plt

def M220607():

  x = np.linspace(0,1,361)
  f = -np.sin(2 * x * np.pi)

  _, ax = plt.subplots(1)

  ax.plot(x,f)
  ax.plot([0.25,0.75,],[-1,1])
  ax.set_xticks([0,0.25,0.5,0.75,1])
  ax.set_xticklabels(['0','$\pi$/4','$\pi$/2','3$\pi$/4','$\pi$'])
  ax.grid()

  plt.savefig(folder + 'M220607.png')

  return plt

if __name__ == '__main__':

  M220607().show()