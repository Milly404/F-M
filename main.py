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

#background 背景照片
background=pygame.image.load(os.path.join(img_folder,"background right.png"))
background_rect=background.get_rect()

#setup palyer 放入人物
#class Player(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.image.load(os.path.join(img_folder,"WuKong 1.png")).convert()

    #def update(self):



#player 人物照片
ship=pygame.image.load(os.path.join(img_folder,"WuKong 1.png"))
ship_rect=ship.get_rect()

#initialize pygame and create window 创造窗户
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FM207")
clock=pygame.time.Clock()

#run game 开始/菜单
while True:
    for event in pygame.event.get():
        #close the window
        if event.type == pygame.QUIT:
            sys.exit

    #draw /render打印背景
    screen.blit(background,background_rect)

    #打印人物
    screen.blit(ship, ship_rect)


    pygame.display.flip()
pygame.quit()

