# a main file that runs an animation with pygame

import time
import pygame
from particle_world import ParticleWorld

def main():

  # set up our own stuff
  p_world = ParticleWorld(36)
  #p_world.plot_lattice()

  # Initialize Pygame
  pygame.init()

  # Set up the screen
  screen_width = 800
  screen_height = 500
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
    scale_x = screen_width / p_world.width
    scale_y = screen_height / p_world.height

    for p in p_world.lattice:
      pygame.draw.rect(screen, WHITE, (p[0] * scale_x, p[1] * scale_y, 10, 10))

    p_world.update()
    time.sleep(.01)

    # Update the display
    pygame.display.flip()

  # Quit Pygame
  pygame.quit()


if __name__ == "__main__":
  main()