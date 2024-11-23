import pygame, sys
from pygame.locals import *
from configs import config

# initiate game engine
pygame.init()

# set up game clock
GameClock = pygame.time.Clock()

# Predefined colors - can we set these up elsewhere?
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Make display
game_display = pygame.display.set_mode(
  size=(config.get('game_configs.screen.width'), config.get('game_configs.screen.width'))
)
game_display.fill(color=WHITE)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  pygame.display.update()
  GameClock.tick()