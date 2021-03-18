# Milly & Fiona
# FM207
# Mar 4 2021

import pygame
import random
import os
from pygame.locals import *
from random import random, randint, seed
import controller

p1 = controller.Controller(0) # into the controller 1

pygame.init()
vInfo = pygame.display.Info()
size = WIDTH, HEIGHT = 1200, 900
FPS = 1
VEL = 10

# images
# find the folder of images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# background
background = pygame.image.load(os.path.join(img_folder, "background right.png"))
background_rect = background.get_rect()

# icon
icon = pygame.image.load(os.path.join(img_folder, "icon.png"))
pygame.display.set_icon(icon)

# player
#run images
player_run = [
    os.path.join(img_folder, "WuKong 1.png"),
    os.path.join(img_folder, "WuKong 2.png"),
    os.path.join(img_folder, "WuKong 3.png"),
    os.path.join(img_folder, "WuKong 4.png"),
]

#jump images
player_jump = [
    os.path.join(img_folder,"WuKong 6.png"),
    os.path.join(img_folder,"WuKong 5.png"),
    os.path.join(img_folder,"WuKong 6.png"),
]

#setup player
class Player(pygame.sprite.Sprite):

   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image=pygame.image.load(os.path.join(img_folder,"WuKong 1.png"))
       self.rect=self.image.get_rect()
       self.level=2
       self.levelChange=10
       self.joystick_pressed = False

   def update(self):
       y1 = 530
       y2 = 675
       y3 = 830

       if self.joystick_pressed == False:
           self.level += p1.get_y_axis()

       if p1.get_y_axis() != 0: # make the play only move one time
           self.joystick_pressed = True
       else:
           self.joystick_pressed = False

       if self.level > 3: # make the play did not move out the road
           self.level = 3
       elif self.level < 1:
           self.level = 1

       if self.level == 1: # make three level for three road
           self.rect.bottom = y1
       elif self.level == 2:
           self.rect.bottom = y2
       else:
           self.rect.bottom = y3

all_sprites=pygame.sprite.Group() #group all of them
player=Player()
all_sprites.add(player) #add player1

# initialize pygame and create window
pygame.init()
# screen=pygame.display.set_mode(size, pygame.NOFRAME)# no frame
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FM207")  # give the game a name

# run game
while True:
    p1.update()

    for event in pygame.event.get(): # close the window
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # close the window with Esc
                sys.exit()

    # draw background
    screen.blit(background, background_rect)

    # draw payer
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    pygame.display.flip()
pygame.quit()