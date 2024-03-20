import numpy as np
from matplotlib import pyplot as plt

class ParticleWorld:
  '''
  Creates a world with periodic boundary conditions
  '''

  def __init__(self, n_particles=36) -> None:
    self.width = int(n_particles ** .5)

    self.n_particles = self.width ** 2

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

    for i in range(self.width):
      for j in range(self.width):
        if self.lattice.size == 0:
          self.lattice = np.append(self.lattice, np.array([i*a1 + j*a2]))
        else:
          self.lattice = np.vstack((self.lattice, np.array([i*a1 + j*a2])))

    self.enforce_periodic_boundary_conditions(self.lattice, [a1, a2], self.width, self.width)
    


  def enforce_periodic_boundary_conditions(self, 
  positions_array, 
  lattice_vectors, 
  x_max, 
  y_max,
  x_min=0, 
  y_min=0):
    '''
    If a particle's position is beyond the x_max, it shifts it back x_max points. 
    NOTE: This is dangerous, because if there are too many particles to fit in 
    the box constrained by x_max and y_max, the particles that fall off the edges
    will go on top of some other particles! It is necessary that somewhere else in code
    we define correctly the size of the box and the number of particles. 
    Perhaps a function that takes in a number of particles and calculates a box that will
    fit them, or vice versa. 
    '''
    for i in range(len(positions_array)):
      pos_x = positions_array[i][0]
      pos_y = positions_array[i][1]

      if pos_x > x_max:
        pos_x -= x_max * lattice_vectors[0][0]
      if pos_y > y_max:
        pos_y -= y_max * lattice_vectors[1][1]

      positions_array[i] = np.array([pos_x, pos_y])


    return positions_array



  def plot_lattice(self):
    print(self.lattice)
    for point in self.lattice:
      plt.plot(point[0], point[1], '.')
    plt.show()


