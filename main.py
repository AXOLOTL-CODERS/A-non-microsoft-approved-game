import pygame
import sys as sus
import random as r
import lib
import time as t

pygame.init()
print('\033[37;2;42m')

start = pygame.time.get_ticks()


dev = False




pygame.time.wait(1000)

print('.....................................................')

pygame.time.wait(1000)

print('\n'*1000)



#--- password ---#
while True:
  password = input('password to the microsoft office trial account:')
  password = password.lower()
  if password == "game":
    break
  elif password == 'dev mode':
    dev = True
    print('guess u want to see a lot of useless junk')
    print('debug mode activated!')
    pygame.time.wait(1000)
  else:
    sus.exit('there is no GAME')


#--- game 1 open ---#
print('YES')

print('(switch to output)')
da_game = pygame.display.set_mode([400,400])

c = pygame.time.Clock()

tim = 0
timlim1 = 5000
points = 0
mxp=1000
autoclickr = 0

looping = True
while looping:
  c.tick(40)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      looping = False
  if event.type == pygame.MOUSEBUTTONDOWN:
    tim += c.get_time()
    points += 1
    points += autoclickr
    print('you have',points)

    if tim >= timlim1:
      upgradelist = input('1. auto clickr is 1000 clicks to get an extra click evry time you click \n 2. storage boost boosts max amount of clicks by 1000 \n 3.retirement fund saves all your clicks to the click net ')
      upgradelist = upgradelist.lower()
      if upgradelist == 'auto clickr' or upgradelist == '1':
        autoclickr += 1
        points - 1000
      elif upgradelist == 'storage boost' or upgradelist == 2:
        mxp += 1000
        points -= 1000
      elif upgradelist == 'retirement fund' or upgradelist == '3':
        input('input username for retirement fund:')
        while looping:
          password = input('input password for retirement fund:')
          if password == 'password':
            looping = False
            
      tim = 0
      if points >= mxp:
        points = mxp
      if points <= -1:
        sus.exit('u lost all your clicks and died unexpectedly')

#--- Story 1 ---#
print('\033[1;37;0; HELLO')
print('IM A HACKER')
print('my name? timmy.')
print('now you need to do things')

#--- Game 2 ---# 
cnum2 = r.randint(0,10)
print('game running: guess the number!!!!')
print('you will guess a number 1-10 you have 5 guesses pls wait') 
print('loading software')
pygame.time.wait(10000)
print('software initalised')
for i in range(5):
  if dev:
    print(cnum2)
  guess = int(input('guess ' + str(i + 1) +':'))
  if guess == cnum2:
    print('you win')
    break
  elif guess != cnum2 and i == 4:
    sus.exit('you suck! num was,' + str(cnum2))

lib.mad_hacker(2)

food=50
cash = 15

is_boosted = False

nobill = False

print('THE MONEY(now with stock)')
while True:
  worker = r.randint(1, 1000)
  bills = r.randint(1,2)
  print("food levels are ",food)
  food-=1
  print('you have $' + str(cash))
  choice1 = input('\033[34minvest/upgrades/work/lottery/donate/buy/cheat/ \033[37m \n')

  if choice1 == 'invest':
        while True:
            choice2 = int(input('how much MONEY do you want to invest '))
            if choice2 <= cash:
                break
        cash -= choice2
        realchoice2 = choice2
        t.sleep(5)
        crash = r.randint(1, 10)
        if crash == 2:
            choice2 *= 5
            print('\u001b[31m \n you lost', realchoice2, 'bucks\u001b[37m ')
            if is_boosted:
                cash = float(cash)
                cash += choice2 / 2
                cash = round(cash)
                cash = int(cash)
                print('you got half back')
        else:
            cash += choice2 * 3

  if choice1 == 'upgrades':
        choice2 = input(
            'what do you want to buy \n \u001b[36m work more $1000 \n \u001b[35m insurance $1,000,000 BUY THIS ONE TIME \u001b[37m \n'
        )
        if choice2 == 'work more':
            worker += 10
            cash -= 1000
        if choice2 == 'insurance':
            print('ok')
            cash -= 1000000
            is_boosted = True

  if choice1 == 'work':
        t.sleep(10)
        cash += worker
        print('you worked and got money')

  if choice1 == 'lottery':
        cash -= 5
        if r.randint(1, 100) == 1:
            print('we have a winner')
            cash += r.randint(1000000, 10000000000)
        else:
            print('\u001b[31m you wasted 5 bucks\u001b[37m ')

  if choice1 == 'donate':
        choice2 = input(
            'would you like to donate to charity or donate to animal shelter? \n'
        )
        if choice2 == 'charity':
            trix = r.randint(1, 10)
            amount = int(input('How much money would you like to donate? \n'))
            cash -= amount
            if trix <= 4:
                t.sleep(4)
                cash += amount * 2
                print(
                    'Since you gave to charity, charity gave back twice the money you donated to them! \n'
                )
        elif choice2 == 'animal shelter':
            trix = r.randint(1, 10)
            if trix <= 4:
                print('Oh no! A Lion stole your money')
                cash = 1
            else:
                print(
                    'You scared the money thief lion. The Animal Shelter payed you for donating to them. \n'
                )
                cash += 1000

  if choice1 == "buy":
        y = input("where would you like to shop food/de mart\n")
        if y == "food":
            fud = input(
                "hello welcome to food mart \n  pizza $7  \n burger $5 \n fries $2 \n sprite $1"
            )
            if fud == "pizza":
                pizza = int(input("how many pizza do you wanna buy"))
                print('successfully bought pizza')
                cash -= 7 * pizza
                food += 7 * pizza
            elif fud == "burger":
                burger = int(input("how many burgers do you wanna get\n"))
                print('successfully bought burger(s)')
                cash -= 5 * burger
                food += 5 * burger
            elif fud == "fries":
                discount = r.randint(1, 10)
                if discount <= 8:
                    fries = int(input("How many fries you want?"))
                    print('Successfully bought fries.')
                    cash -= 2 * fries
                elif discount <= 10:
                    print('You got free fries! Discount, woo!')
            elif fud == "sprite":
                print(
                    'box of sprite $12 \n normal sprite can $1\n plastic sprite bottle $3 \n big sprite bottle (party size) $11\n'
                )
                q = input("choose")
                if q == "box of sprite":
                    cash -= 12
                    ('bought box of cans (sprite)')
                elif q == "normal sprite can" or q == "sprite can":
                    sprite = int(input('how many sprite cans you want?\n'))
                    cash -= 1 * sprite
                    print('successfuly bought')
                elif q == "big sprite bottle":
                  sprite = int(input('How many big bottles do you want? \n'))
                  cash -= 11 * sprite
                  print ('successfully bought the party size sprite bottle \n')
                elif q == "plastic sprite bottle":
                  cash -= 3
                  print ('Successfully bought')
        elif y == 'de mart':
          print ('De Mart is currently under construction, sorry.')


  if bills == 2 and not nobill:
        pay = input('You need to pay your bills. Will you? ')
        if pay != "yes":
            cash = 0
            print('You did not pay your bills and the IRS took your money. and you died unexpectedly')
            sus.exit("PAY.YOUR.BILLS.")
        else:
            vary = r.randint(1, 10)
            if vary <= 9:
                cash -= 10
            else:
                cash -= 15
        if cash == 0:
            cash = 10

  if cash <= 0:
        sus.exit("you're broke")



