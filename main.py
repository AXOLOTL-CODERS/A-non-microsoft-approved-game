import random as r
import pygame
import sys as sus
pygame.init()
start = pygame.time.get_ticks()

dev = False


print('sorta a ripoff of there is no game by kasimoto')
pygame.time.wait(1000)

print('not loading')

pygame.time.wait(1000)

print('\n'*1000)
print("Hello User")
pygame.time.wait(1000)
print('I. I have bad News')
pygame.time.wait(1000)
print('this is not a clicker game')
pygame.time.wait(1000)
print('it has nothing to do with a game')
pygame.time.wait(1000)
print('it\'s just a massive pakage of bordum')
pygame.time.wait(1000)
print('THIS IS NOT A GAME')
pygame.time.wait(1000)
print('it has nothing to do with a game')



# password
while True:
  password = input('password to the massive pakage of bordom:')
  password = password.lower()
  if password == "game":
    break
  elif password == 'debug mode':
    dev = True
  else:
    sus.exit('there is no GAME')




print('no, no no no')

print('(switch to output)')
da_game = pygame.display.set_mode([400,300])

c = pygame.time.Clock()

tim = 0
timlim1 = 5000
points = 0

looping = True
while looping:
  c.tick(40)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      looping = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      points += 1
      print('you have',points)
      
