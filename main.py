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
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

#background 背景照片导入
background=pygame.image.load(os.path.join(img_folder,"background right.png"))
background_rect=background.get_rect()

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

#setup player
class Player(pygame.sprite.Sprite):
   #sprite for the player

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

       self.sprites_jump=player_jump
       self.current_sprite_jump = 1
       self.image = self.sprites_jump[self.current_sprite_jump]
       self.rect = self.image.get_rect()

       self.rect.center=139,602
       self.y_speed=1
       self.rect.bottom=830
       self.level=2
       self.levelChange=10
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

   def jump(self,speed):
       self.allow_jump=False

       global FPS

       self.animation_counter += 1

       if self.animation_counter == self.frame_ratio:
           self.animation_counter = 0
           self.current_sprite_jump += speed

       if int(self.current_sprite_jump) >= len(self.sprites_jump):
           self.current_sprite_jump = 0
       self.image = self.sprites_jump[int(self.current_sprite_jump)]



   def update(self):

       self.run_animation(1)

       self.y_speed=0
       keys=pygame.key.get_pressed()

       if self.joystick_pressed == False:
           self.level += p1.get_y_axis()

       if p1.get_y_axis() != 0:
           self.joystick_pressed = True
       else:
           self.joystick_pressed = False

       # if p1.is_button_just_pressed("a"):
       #     self.level += 1
       # elif p1.is_button_just_pressed("b"):
       #     self.level -= 1

       if self.level > 3:
           self.level = 3
       elif self.level < 1:
           self.level = 1

       if self.level == 1:
           self.rect.bottom = y1
       elif self.level == 2:
           self.rect.bottom = y2
       else:
           self.rect.bottom = y3

       if p1.is_button_just_pressed("a"):
           self.jump(1)
           self.rect.bottom-=30

       # if event.type==pygame.KEYDOWN:
       #     if event.key==pygame.K_UP:
       #         if self.rect.bottom==y2 or y1:
       #             self.rect.bottom=y1
       #         if self.rect.bottom==y3:
       #             self.rect.bottom=y2
       #     elif event.key==pygame.K_DOWN:
       #         if self.rect.bottom==y2 or y3:
       #             self.rect.bottom=y3
       #         if self.rect.bottom==y1:
       #             self.rect.bottom=y2
       #     elif event.type==pygame.KEYUP:
       #         player_movey=1
       # elif event.type==pygame.KEYUP:
       #     if event.key==pygame.K_UP:
       #          if self.rect.bottom == y2:
       #              self.rect.bottom = y2
       #          if self.rect.bottom == y3:
       #              self.rect.bottom = y3
       #          if self.rect.bottom==y1:
       #              self.rect.bottom=y1
       #     elif event.key==pygame.K_DOWN:
       #         if self.rect.bottom == y2:
       #             self.rect.bottom = y2
       #         if self.rect.bottom == y3:
       #             self.rect.bottom = y3
       #         if self.rect.bottom == y1:
       #             self.rect.bottom = y1


class obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = obstacle_img
        self.current_sprite = randint(0,3)
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        y1=randint(0,2)*150+600
        self.rect.bottomleft = (randint(970,10000),y1)
        self.start_time=pygame.time.get_ticks()

    def update(self):
        if self.start_time and pygame.time.get_ticks()-self.start_time>2000:
            self.start_time=False
        self.rect.x-=5


all_sprites=pygame.sprite.Group() #group all of them
player=Player()
all_sprites.add(player) #add player1

for Obstacle in range(1,50):
    Obstacle=obstacle()
    all_sprites.add(Obstacle) #add obstacle

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
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
pygame.quit()