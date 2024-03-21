# a main file that runs an animation with pygame

import pygame
from particle_world import ParticleWorld

def main():

  # set up our own stuff
  p_world = ParticleWorld(36)
  p_world.plot_lattice()
  scale = 100
  offset = 10

  # Initialize Pygame
  pygame.init()

  # Set up the screen
  screen_width = p_world.width * 1.5 * scale
  screen_height = p_world.width * 1.5 * scale
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Molecular Dynamics")

  # Set up colors
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)


  # Main game loop
  running = True
  while running:
    # Event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # draw the particles NOTE: y=0 is at the top of the screen, not the bottom
    scale = 150

    for p in p_world.lattice:
      pygame.draw.rect(screen, WHITE, (p[0] * scale + offset, p[1] * scale + offset, 10, 10))


    # Update the display
    pygame.display.flip()

  # Quit Pygame
  pygame.quit()


if __name__ == "__main__":
  main()