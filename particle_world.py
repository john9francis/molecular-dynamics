import numpy as np
from matplotlib import pyplot as plt

class ParticleWorld:
  '''
  Creates a world with periodic boundary conditions
  '''

  def __init__(self) -> None:
    self.x_size = 4.3
    self.y_size = 4.3

    self.lattice = np.array([0, 0])

    self.create_lattice()
    self.plot_lattice()

    pass


  def create_lattice(self):
    '''
    Generate a triangular lattice using basis vectors
    1.07457*(1,0) and 1.07457*(.5, .8660254)
    '''

    a1 = 1.07457 * np.array([1, 0])
    a2 = 1.07457 * np.array([.5, .8660254])

    for i in range(4):
      for j in range(4):
        self.lattice = np.vstack((self.lattice, np.array([i*a1 , j*a2])))

    pass


  def plot_lattice(self):
    print(self.lattice)
    plt.plot(self.lattice, '.')
    plt.show()


