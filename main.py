# Milly & Fiona
# FM207
# Mar 4 2021

import pygame
import random
import os
from random import random, randint, seed

WIDTH=1200
HEIGHT=900
FPS=258
VEL=10

#images 照片
#find the folder of images 找到我们可爱的照片文件夹
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

#background 背景
brackground=pygame.image.load(os.path.join(img_folder,"background right.png"))
brackground_rect=brackground.get_rect()

#setup palyer
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(img_folder,"WuKong 1.png")).convert()


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FM207")
clock=pygame.time.Clock()

screen.blit(brackground,brackground_rect)