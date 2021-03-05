# Milly & Fiona
# FM207
# Mar 4 2021

import pygame
import random
import os
from random import random, randint, seed

WIDTH=800
HEIGHT=600
FPS=258
VEL=10

#images 照片
#find the folder of images 找到我们可爱的照片文件夹
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

#background 背景
brackground=pygame.image.load(os.path.join(img_folder,".png"))
brackground_rect=brackground.get_rect()

#