import numpy as np
from matplotlib import pyplot as plt

class ParticleWorld:
  '''
  Creates a world with periodic boundary conditions
  '''

  def __init__(self, n_particles=25) -> None:
    self.n_particles = int(n_particles ** .5) ** 2

    # width and height will be defined in self.create_lattice
    self.width = 0 
    self.height = 0

    # self.lattice = self.create_random_lattice()
    self.lattice = self.create_random_lattice()

    self.v0 = 1
    self.dt = .001

    self.velocities = np.empty_like(self.lattice)
    self.velocities = self.create_random_velocities(self.v0, self.velocities)
    self.previous_lattice = self.lattice - self.velocities * self.dt
    self.next_lattice = np.empty_like(self.lattice)

    #print("Initial velocities:")
    #print(self.velocities)



  def create_lattice(self) -> np.ndarray:
    '''
    Generate a triangular lattice using basis vectors
    1.07457*(1,0) and 1.07457*(.5, .8660254)
    '''

    a1 = 1.07457 * np.array([1, 0])
    a2 = 1.07457 * np.array([.5, .8660254])

    new_lattice = np.array([])

    n = int(self.n_particles ** .5)

    for i in range(n):
      for j in range(n):
        if new_lattice.size == 0:
          new_lattice = np.append(new_lattice, np.array([i*a1 + j*a2]))
        else:
          new_lattice = np.vstack((new_lattice, np.array([i*a1 + j*a2])))

    # set width and height
    scale = 1
    self.width = scale * n * a1[0]
    self.height = scale * n * a2[1]

    offset = .5

    new_lattice = new_lattice + offset

    return self.enforce_periodic_boundary_conditions(new_lattice)
    

  def create_random_lattice(self, not_random_lattice:np.ndarray=None) -> np.ndarray:
    '''
    Takes in a lattice and randomizes it a bit
    '''
    if not_random_lattice == None:
      random_lattice = self.create_lattice()
    else:
      random_lattice = np.copy(not_random_lattice)

    for i in range(len(random_lattice)):
      r = np.random.uniform(0, 0.01)
      theta = np.random.uniform(0, 2 * np.pi)
      x = r * np.cos(theta)
      y = r * np.sin(theta)

      random_lattice[i] = random_lattice[i] + np.array([x, y])

    return random_lattice



  def enforce_periodic_boundary_conditions(self, positions_array):
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

      if pos_x > self.width:
        pos_x -= self.width
      if pos_x < 0:
        pos_x += self.width
        
      if pos_y > self.height:
        pos_y -= self.height
      if pos_y < 0:
        pos_y += self.height

      positions_array[i] = np.array([pos_x, pos_y])


    return positions_array



  def plot_lattice(self):
    for point in self.lattice:
      plt.plot(point[0], point[1], '.')
    plt.show()


  def create_random_velocities(self, init_v, v_array):
    '''
    Creates an array of random velocities all around init_v
    '''
    for i in range(len(v_array)):
      v_array[i][0] = 2 * (np.random.uniform(0, 1) - .5) * init_v
      v_array[i][1] = 2 * (np.random.uniform(0, 1) - .5) * init_v

    return v_array


  def lennard_jones_force(self, r):
    '''
    Takes in a distance r and calculates the
    lennard jones potential force
    '''
    return 24 * (2 / (r ** 13) - 1 / (r ** 7))


  def get_periodic_r_array(self, positions_array, particle_indx):
    '''
    Gets the array r values, including the periodic boundary conditions
    to get the "closest" r for each particle.
    '''
    # copy to not affect the original array
    pos_array = np.copy(positions_array)

    # grab the particle pos for later
    particle_pos = pos_array[particle_indx]

    # check the radii between the particle and the other positions
    for i, pos in enumerate(pos_array):
      if i == particle_indx:
        continue
      
      


    for i, pos in enumerate(pos_array):

      r = abs(particle_pos - pos_array[i])
      if r[0] > self.width / 2:
        pos_array[i] += self.width
      if r[1] > self.height / 2:
        pos_array[i] += self.height

    for i, pos in enumerate(pos_array):

      r = abs(particle_pos - pos_array[i])
      if r[0] > self.width / 2:
        pos_array[i] -= 2 * self.width
      if r[1] > self.height / 2:
        pos_array[i] -= 2 * self.height

    return particle_pos - pos_array
      
    


  def calculate_net_force(self, particle_pos_list, particle_indx, box_size) -> np.ndarray:
    '''
    Takes in a particle index and calculates the net
    force on that particle from the other particles
    returns a vector of [force_x, force_y]
    '''
    # set the maximum r, above this, force = 0
    rcut = 3

    # check for errors
    if particle_indx > len(self.lattice):
      print("!!!get_f_on_particle error!!! trying to get particle indx out of bounds")
      return None


    r_vectors = self.get_periodic_r_array(particle_pos_list, particle_indx)

    # Calculate total force now
    total_force = np.array([0,0])
    for r in r_vectors:
      r_mag = (r[0]**2 + r[1]**2)**.5

      # skip if the r is too big
      if r_mag > rcut:
        continue

      direction = r / r_mag

      force = self.lennard_jones_force(r_mag) * direction

      total_force = total_force + force

    return total_force


  def calculate_force_array(self, pos_array):
    '''
    Returns an array of all the forces
    '''
    all_force_list = []

    for i in range(len(pos_array)):
      new_f = self.calculate_net_force(pos_array, i, self.width)
      all_force_list.append(new_f)

    
    return np.array(all_force_list)



  def update(self):
    '''
    Updates positions based on the verlet method
    '''
    f = self.calculate_force_array(self.lattice)
    self.next_lattice = 2 * self.lattice - self.previous_lattice + f * self.dt ** 2
    self.next_lattice = self.enforce_periodic_boundary_conditions(self.next_lattice)
 
    # finally, reset the lattice variable
    self.previous_lattice = np.copy(self.lattice)
    self.lattice = np.copy(self.next_lattice)

