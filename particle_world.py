import numpy as np
from matplotlib import pyplot as plt

class ParticleWorld:
  '''
  Creates a world with periodic boundary conditions
  '''

  def __init__(self) -> None:
    self.x_size = 4.3
    self.y_size = 4.3

    self.lattice = np.array([])

    self.create_lattice()
    self.plot_lattice()



  def create_lattice(self):
    '''
    Generate a triangular lattice using basis vectors
    1.07457*(1,0) and 1.07457*(.5, .8660254)
    '''

    a1 = 1.07457 * np.array([1, 0])
    a2 = 1.07457 * np.array([.5, .8660254])

    for i in range(1,5):
      for j in range(1,5):
        if self.lattice.size == 0:
          self.lattice = np.append(self.lattice, np.array([i*a1 + j*a2]))
        else:
          self.lattice = np.vstack((self.lattice, np.array([i*a1 + j*a2])))



  def plot_lattice(self):
    print(self.lattice)
    for point in self.lattice:
      plt.plot(point[0], point[1], '.')
    plt.show()


