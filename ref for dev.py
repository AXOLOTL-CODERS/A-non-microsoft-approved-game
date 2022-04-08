import pygame

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    running = False
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K.keyname:
      code
    if event.key == pygame.K_keyname:
      code