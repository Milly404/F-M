# Milly & Fiona
# FM207
# Mar 4 2021

import pygame
import random
import os
from random import random, randint, seed

pygame.init()
vInfo = pygame.display.Info()
#size = WIDTH, HEIGHT = vInfo.current_w, vInfo.current_h #适合大小
size = WIDTH, HEIGHT = 1200,900 #固定大小
FPS=258
VEL=10
BLACK = 0,0,0

#images 照片
#find the folder of images 找到我们可爱的照片文件夹
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

#background 背景照片导入
background=pygame.image.load(os.path.join(img_folder,"background right.png"))
background_rect=background.get_rect()

#icon 图标导入
icon = pygame.image.load(os.path.join(img_folder,"icon.png"))
pygame.display.set_icon(icon)

#player 人物照片导入
WuKong1=pygame.image.load(os.path.join(img_folder,"WuKong 11.png"))
WuKong1_rect=WuKong1.get_rect()
Wukong=WUkong_x,Wukong_y=139,602   #7,602

#initialize pygame and create window 创造窗口
pygame.init()
#screen=pygame.display.set_mode(size, pygame.RESIZABLE) #可移动的屏幕有机会再说
#screen=pygame.display.set_mode(size, pygame.NOFRAME)#无边框
#screen=pygame.display.set_mode(size, pygame.FULLSCREEN) #诶嘿搞个全屏就快乐了
screen=pygame.display.set_mode(size)
pygame.display.set_caption("FM207") #give the game a name 给它个名字

#run game 开始冲冲冲
while True:
    for event in pygame.event.get():
        #close the window
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #close the window with Esc
                sys.exit()
            #if event.key == pygame.K_UP:

            #elif event.key == pygame.K_DOWN:


        # 测试xy轴
        #elif event.type == pygame.MOUSEMOTION:#鼠标所在位置
            #print("[MOUSEMOTION]:", event.pos,event.rel, event.buttons)
        #elif event.type == pygame.MOUSEBUTTONUP:#鼠标释放
            #print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:#鼠标点击
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)

        # 可移动并保持移动的窗口
        #elif event.type == pygame.VIDEORESIZE:
            #size = WIDTH,HEIGHT = event.size[0],event.size[1]
            #screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    #draw /render打印背景
    screen.blit(background,background_rect)

    #打印人物
    screen.blit(WuKong1, Wukong)

    pygame.display.update()
    pygame.display.flip()
pygame.quit()


