#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
pygame.init()


class Snake(object):
    """docstring for snake."""

    def __init__(self):

        """Colors """
        self.green =(132, 169, 108)
        self.red = (255,0,0)
        self.grey = (40,44,52)
        """Border"""
        self.hight = 1280
        self.width = 720
        """Start"""
        self.x = self.hight/2
        self.y = self.width/2

        self.x_change = 0
        self.y_change = 0

        """Snake Parameters"""
        self.snake_size = 15
        self.snake_speed = 25

        self.clock = pygame.time.Clock()
        self.game_over = False

        self.display_game = pygame.display.set_mode((self.hight,self.width))
        pygame.display.set_caption('Snake Game')

    def gameOver(self):
        game_over = True
        if __name__ == "modules.snake":
            app = QApplication(sys.argv)
            window = Popup()
            window.interface_Game_Over()
            sys.exit(app.exec_())
            pygame.quit()
            exit()


    def update_window(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change = -self.snake_size
                        self.y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x_change = self.snake_size
                        self.y_change = 0
                    elif event.key == pygame.K_UP:
                        self.x_change = 0
                        self.y_change = -self.snake_size
                    elif event.key == pygame.K_DOWN:
                        self.x_change = 0
                        self.y_change = self.snake_size
                    elif event.key == pygame.K_SPACE:
                        self.x_change = 0
                        self.y_change = 0

            if self.y >= self.width or self.x <= 0 or self.x >= self.hight or self.y <= 0:
                self.gameOver()

            self.x += self.x_change
            self.y += self.y_change

            self.display_game.fill(self.grey)
            pygame.draw.rect(self.display_game,self.green,[self.x,self.y,self.snake_size,self.snake_size])
            pygame.display.update()
            self.clock.tick(self.snake_speed)
