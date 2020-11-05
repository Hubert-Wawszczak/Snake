import pygame
from pygame.locals import *
pygame.init()

green =(0,255,0)
red = (255,0,0)
white =(0,0,0)

a=800
b=600

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

game_over = False
display_game=pygame.display.set_mode((a,b))
pygame.display.update()
pygame.display.set_caption('Snake Game')

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    display_game.fill(white)
    pygame.draw.rect(display_game,green,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
