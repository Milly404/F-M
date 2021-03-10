# Milly & Fiona
# FM207
# Mar 4 2021

import pygame
import random
import os
from pygame.locals import *
from random import random, randint, seed
import controller

pygame.init()
vInfo = pygame.display.Info()
size = WIDTH, HEIGHT = 1200, 900
FPS = 258
VEL = 10
BLACK = 0, 0, 0

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
WuKong1 = pygame.image.load(os.path.join(img_folder, "WuKong 1.png"))
WuKong1_rect = WuKong1.get_rect()

class Player:

    def __init__(self, WuKong1):
        self.x = 139
        self.y = 602



# initialize pygame and create window
pygame.init()
# screen=pygame.display.set_mode(size, pygame.NOFRAME)# no frame
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FM207")  # give the game a name

# run game
while True:
    for event in pygame.event.get():
        # close the window
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # close the window with Esc
                sys.exit()


    # draw background
    screen.blit(background, background_rect)

    # draw payer
    screen.blit(WuKong1, WuKong1_rect)

    pygame.display.update()
    pygame.display.flip()
pygame.quit()
