# Milly & Fiona
# FM207
# Mar 4 2021

import pygame,sys
import random
import os
from random import random, randint, seed
import controller
from time import sleep

p1 = controller.Controller(0)

pygame.init()
vInfo = pygame.display.Info()
#size = WIDTH, HEIGHT = vInfo.current_w, vInfo.current_h #适合大小
size = WIDTH, HEIGHT = 1200,900 #固定大小
FPS=30
VEL=10
y1 = 530
y2 = 675
y3 = 830
BLACK = 0,0,0

#images 照片
#find the folder of images 找到我们可爱的照片文件夹
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

#background 背景照片导入
bg1 = pygame.image.load(os.path.join(img_folder,"background right.png"))
bg2 = pygame.image.load(os.path.join(img_folder,"background right.png"))

x1 = 0
x2 = -1200

#icon 图标导入
icon = pygame.image.load(os.path.join(img_folder,"icon.png"))
pygame.display.set_icon(icon)

#obstacle 障碍导入
stone=pygame.image.load(os.path.join(img_folder,"Stone.png"))
stone_rect=stone.get_rect()

#player 人物照片导入
# WuKong1=pygame.image.load(os.path.join(img_folder,"WuKong 1.png"))
# WuKong1_rect=WuKong1.get_rect()
# Wukong=WUkong_x,Wukong_y=139,602   #7,602

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

#obstacle images
obstacle_img = []
obstacle_img.append(pygame.image.load('img\Stone.PNG'))
obstacle_img.append(pygame.image.load('img\HuLu.PNG'))
obstacle_img.append(pygame.image.load('img\JingJiaoDaWang.PNG'))
obstacle_img.append(pygame.image.load('img\PanTao.PNG'))

#initialize pygame and create window 创造窗口
pygame.init()
clock = pygame.time.Clock()
#screen=pygame.display.set_mode(size, pygame.RESIZABLE) #可移动的屏幕有机会再说
#screen=pygame.display.set_mode(size, pygame.NOFRAME)#无边框
#screen=pygame.display.set_mode(size, pygame.FULLSCREEN) #诶嘿搞个全屏就快乐了
screen=pygame.display.set_mode(size)
pygame.display.set_caption("FM207") #give the game a name 给它个名字

def bg_move():

    global x1,x2

    x1 -= 1
    x2 -= 1

    screen.blit(bg1, (x1,0))
    screen.blit(bg2, (x2, 0))

    if x1 < -1200:
        x1 = 1200
    if x2 < -1200:
        x2 = 1200

    return x1, x2

#run game 开始冲冲冲
while True:

    clock.tick(FPS)

    p1.update()

    for event in pygame.event.get():
        #close the window
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE: #close the window with Esc
                sys.exit()


    #draw /render打印背景
    x1, x2 = bg_move()



    pygame.display.update()
pygame.quit()

