import pygame
import math

pygame.init()
fps = 60
timer = pygame.time.clock()
font = pygame.font.font('assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 0
for i in range(1,4):
    bgs.append(pygame.image.loaf(f'assets/bgs/{i}.png'))
    banners.append(pygame.image.loaf(f'assets/bgs/{i}.png'))
    guns.append(pygame.image.loaf(f'assets/bgs/{i}.png'))