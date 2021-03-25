import pygame,sys

player_run = []
player_run.append(pygame.image.load('img\WuKong 1.png'))
player_run.append(pygame.image.load('img\WuKong 2.png'))
player_run.append(pygame.image.load('img\WuKong 3.png'))
player_run.append(pygame.image.load('img\WuKong 4.png'))

#jump images
player_jump = []
player_jump.append(pygame.image.load('img\WuKong 6.png'))
player_jump.append(pygame.image.load('img\WuKong 5.png'))
player_jump.append(pygame.image.load('img\WuKong 6.png'))




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

   def jump(self):

       global FPS




   def update(self):

       self.run_animation(1)

       self.y_speed=0
       keys=pygame.key.get_pressed()



# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


  # Drawing
  screen.fill((0,0,0))
  moving_sprites.draw(screen)
  moving_sprites.update(0.25)
  pygame.display.flip()
  clock.tick(60)

