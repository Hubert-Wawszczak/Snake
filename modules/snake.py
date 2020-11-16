#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
import time
pygame.init()


class Snake(object):
    """docstring for snake."""

    def __init__(self):

        """Colors """
        self.green =(132, 169, 108)
        self.red = (255,0,0)
        self.grey = (40,44,52)
        """Border"""
        self.hight = 800
        self.width = 600
        """Start"""
        self.x = self.hight/2
        self.y = self.width/2

        self.x_change = 0
        self.y_change = 0

        """Snake Parameters"""
        self.snake_size = 20
        self.snake_speed = 5

        self.clock = pygame.time.Clock()
        self.game_over = False

        self.display_game = pygame.display.set_mode((self.hight,self.width))
        pygame.display.set_caption('Snake Game')

        """FOOD"""
        self.food_X = round(random.randrange(0,self.hight - self.snake_size)/self.snake_size)*self.snake_size
        self.food_Y = round(random.randrange(0,self.width - self.snake_size)/self.snake_size)*self.snake_size

        self.snake_List = []
        self.length_of_snake = 1

    def render_Snake(self,snake_size, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.display_game,self.green,[x[0],x[1],self.snake_size,self.snake_size])


    def gameOver(self):
        game_over = True
        pygame.quit()
        quit()

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

            pygame.draw.rect(self.display_game,self.red,[self.food_X,self.food_Y,self.snake_size,self.snake_size])

            snake_Head =[]
            snake_Head.append(self.x)
            snake_Head.append(self.y)
            self.snake_List.append(snake_Head)

            if len(self.snake_List) > self.length_of_snake:
                del self.snake_List[0]

            for x in self.snake_List[:-1]:
                if x == snake_Head:
                    self.gameOver()

            self.render_Snake(self.snake_size, self.snake_List)

            pygame.display.update()

            if self.x == self.food_X and self.y == self.food_Y:
                self.food_X = round(random.randrange(0,self.hight - self.snake_size)/self.snake_size)*self.snake_size
                self.food_Y = round(random.randrange(0,self.width - self.snake_size)/self.snake_size)*self.snake_size
                self.length_of_snake += 1
                self.snake_speed += 1

            self.clock.tick(self.snake_speed)
