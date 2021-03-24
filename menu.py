import pygame, sys
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

menu = pygame.image.load(os.path.join(img_folder,"menu.png"))
menu_rect = menu.get_rect()

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1200, 900), 0, 32)

font = pygame.font.SysFont('Time New Roman', 45)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.blit(menu,menu_rect)


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(500, 650, 100, 45)

        if button_1.collidepoint((mx, my)):
            if click:
                game()

        pygame.draw.rect(screen, (194, 221, 239), button_1)
        draw_text('Start', font, (0, 0, 0), screen, 514, 658)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
