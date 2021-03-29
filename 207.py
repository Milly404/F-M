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
game_over = True
running = True
font = pygame.font.SysFont('Arial', 45)

# images
# find the folder of images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#menu images
menu = pygame.image.load(os.path.join(img_folder,"menu.png"))
menu_rect = menu.get_rect()

# background images
bg1 = pygame.image.load(os.path.join(img_folder,"background left.png"))
bg2 = pygame.image.load(os.path.join(img_folder,"background left.png"))
x1 = 0
x2 = -1200

# icon images
icon = pygame.image.load(os.path.join(img_folder, "icon.png"))
pygame.display.set_icon(icon)

# player images
# run images
player_run = []
player_run.append(pygame.image.load('img\WuKong 1.png'))
player_run.append(pygame.image.load('img\WuKong 2.png'))
player_run.append(pygame.image.load('img\WuKong 3.png'))
player_run.append(pygame.image.load('img\WuKong 4.png'))
player_run.reverse()

# jump images
player_jump = []
player_jump.append(pygame.image.load('img\WuKong 6.png'))
player_jump.append(pygame.image.load('img\WuKong 5.png'))
player_jump.append(pygame.image.load('img\WuKong 6.png'))

# obstacle images
obstacle_img = []
obstacle_img.append(pygame.image.load('img\Stone.PNG'))
obstacle_img.append(pygame.image.load('img\HuLu.PNG'))
obstacle_img.append(pygame.image.load('img\JingJiaoDaWang.PNG'))
obstacle_img.append(pygame.image.load('img\PanTao.PNG'))

def draw_text(text, font, color, surface, x, y): #show the text
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def show_go_screen(): #start menu
    screen.blit(menu, menu_rect)
    draw_text('Press  (A)  to  start', font, (45, 95, 204), screen, 420, 658)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def bg_move(): #bargound moving

    global x1,x2

    x1 -= 3
    x2 -= 3

    screen.blit(bg1, (x1, 0))
    screen.blit(bg2, (x2, 0))

    if x1 < -1200:
        x1 = 1200
    if x2 < -1200:
        x2 = 1200

    return x1, x2

#setup player
class Player(pygame.sprite.Sprite): #add the player

   def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       super().__init__()
       self.animation_speed = 8
       self.animation_counter = 0
       self.frame_ratio = int(FPS / self.animation_speed)
       self.sprites = player_run
       self.current_sprite = 0
       self.image = self.sprites[self.current_sprite]
       self.rect = self.image.get_rect()
       self.radius = int(self.rect.width / 2.4)

       self.rect.center = 139, 602
       self.y_speed = 1
       self.rect.bottom = 830
       self.level = 2
       self.levelChange = 10
       self.joystick_pressed = False

   def run_animation(self,speed): # make the picture change like play are running

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

class obstacle(pygame.sprite.Sprite): #add the obstacle

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = obstacle_img
        self.current_sprite = randint(0,3)
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2.5)
        y1=randint(0,2)*150+560 # made them randint in three level
        self.rect.bottomleft = (randint(970,1000000),y1)
        self.start_time=pygame.time.get_ticks()

    def update(self):
        if self.start_time and pygame.time.get_ticks()-self.start_time>2000:
            self.start_time=False
        self.rect.x-=5 #moving to the laft by 5 speeds

# initialize pygame and create window
pygame.init()
clock = pygame.time.Clock()
# screen=pygame.display.set_mode(size, pygame.NOFRAME)# no frame
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FM207")  # give the game a name

# run game
while True:

    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()  # group all of them
        obstacles = pygame.sprite.Group()
        for Obstacle in range(1, 10000):
            Obstacle = obstacle()
            all_sprites.add(Obstacle)  # add obstacle
            obstacles.add(Obstacle)
        player = Player()
        all_sprites.add(player)  # add player1

    clock.tick(FPS)

    p1.update()

    for event in pygame.event.get(): # close the window
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # close the window with Esc
                sys.exit()

    # draw background
    x1, x2 = bg_move()

    # draw payer
    all_sprites.update()


    #check to see if hit
    hits = pygame.sprite.spritecollide(player, obstacles, False, pygame.sprite.collide_circle)
    if hits:
        game_over = True

    all_sprites.draw(screen)

    pygame.display.update()
    pygame.display.flip()
pygame.quit()