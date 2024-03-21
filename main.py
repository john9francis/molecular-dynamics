from particle_world import ParticleWorld
import numpy as np

def main():
  p = ParticleWorld()
  box_size = 5

  # RECREATE TABLE:
  positions = np.array([[4,4],[3.5,1.5],[0.5,2]])

  print("Location:     Net force:")
  for i in range(len(positions)):
    print(f"{positions[i]}, {p.calculate_net_force(positions, i, box_size)}")

if __name__ == "__main__":
  main()