# Milly & Fiona
# FM207
# Mar 4 2021

import pygame,sys
import random
import os
from pygame.locals import *
from random import random, randint, seed
import controller

p1 = controller.Controller(0) # into the controller 1

pygame.init()
vInfo = pygame.display.Info()
size = WIDTH, HEIGHT = 1200, 900
FPS = 30
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
player_run = []
player_run.append(pygame.image.load('img\WuKong 1.png'))
player_run.append(pygame.image.load('img\WuKong 2.png'))
player_run.append(pygame.image.load('img\WuKong 3.png'))
player_run.append(pygame.image.load('img\WuKong 4.png'))
player_run.reverse()

#jump images
player_jump = []
player_jump.append(pygame.image.load('img\WuKong 6.png'))
player_jump.append(pygame.image.load('img\WuKong 5.png'))
player_jump.append(pygame.image.load('img\WuKong 6.png'))

#setup player
class Player(pygame.sprite.Sprite):

   def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       super().__init__()
       #self.run_animation = False
       self.animation_speed = 8
       self.animation_counter = 0
       self.frame_ratio = int(FPS/self.animation_speed)
       self.sprites = player_run
       self.current_sprite = 0
       self.image = self.sprites[self.current_sprite]
       self.rect = self.image.get_rect()

       self.image=pygame.image.load(os.path.join(img_folder,"WuKong 1.png"))
       self.rect=self.image.get_rect()
       self.level=2
       self.joystick_pressed = False

   def run_animation(self,speed):

       global FPS

       self.animation_counter += 1

       if self.animation_counter == self.frame_ratio:
           self.animation_counter = 0
           self.current_sprite += speed

       if int(self.current_sprite) >= len(self.sprites):
           self.current_sprite = 0
       self.image = self.sprites[int(self.current_sprite)]

   def update(self):

       self.run_animation(1)

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
clock = pygame.time.Clock()
# screen=pygame.display.set_mode(size, pygame.NOFRAME)# no frame
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FM207")  # give the game a name

# run game
while True:
    clock.tick(FPS)

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