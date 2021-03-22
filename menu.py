import pygame
import controller
import os

pygame.init()
vInfo = pygame.display.Info()
size = WIDTH, HEIGHT = 1200,900
FPS=30
VEL=10
y1 = 530
y2 = 675
y3 = 830
BLACK = (0,0,0)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FM207")

def StartMenu(self, screen, text='Press (UP) To Start'):
    self.image = pygame.image.load(os.path.join(img_folder, "menu.png"))
    self.rect = self.image.get_rect()
    screen.fill()
    pygame.display.update()
    self.fill_text(screen)
    font_size = 24
    font = pygame.font.SysFont('arial', font_size)
    font_width, font_height = font.size(str(text))
    screen.blit(font.render(str(text), True, BLACK), (554, 753))

while True:
    StartMenu()
    pygame.display.update()
pygame.quit()
