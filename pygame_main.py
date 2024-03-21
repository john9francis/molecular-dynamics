# a main file that runs an animation with pygame

import pygame

def main():

  # Initialize Pygame
  pygame.init()

  # Set up the screen
  screen_width = 800
  screen_height = 600
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

    # Update the display
    pygame.display.flip()

  # Quit Pygame
  pygame.quit()


if __name__ == "__main__":
  main()