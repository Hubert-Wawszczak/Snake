import pygame
from pygame.locals import *
pygame.init()



class snake(object):
    """docstring for snake."""

    def __init__(self):
        super(snake, self).__init__()

        self.green =(132, 169, 108)
        self.red = (255,0,0)
        self.grey = (40,44,52)

        self.hight = 1280
        self.width = 720

        self.start_x = self.hight/2
        self.start_y = self.width/2

        self.x_change = 0
        self.y_change = 0

        self.clock = pygame.time.Clock()
        self.game_over = False

        self.display_game = pygame.display.set_mode((self.hight,self.width))

    def update_window(self):
        pygame.display.set_caption('Snake Game')
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change = -10
                        self.y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x_change = 10
                        self.y_change = 0
                    elif event.key == pygame.K_UP:
                        self.x_change = 0
                        self.y_change = -10
                    elif event.key == pygame.K_DOWN:
                        self.x_change = 0
                        self.y_change = 10
                    elif event.key == pygame.K_SPACE:
                        self.x_change = 0
                        self.y_change = 0

            self.start_x += self.x_change
            self.start_y += self.y_change

            self.display_game.fill(self.grey)
            pygame.draw.rect(self.display_game,self.green,[self.start_x,self.start_y,15,15])
            pygame.display.update()
            self.clock.tick(25)


a = snake()
a.update_window()
