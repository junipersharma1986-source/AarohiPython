import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
  for event in pygame.event.get():

     if event.type == pygame.QUIT:
       done = True

  pygame.draw.circle(screen, (255, 192, 203), (200, 150), 50)
  pygame.display.flip()