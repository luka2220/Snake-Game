# program for my snake game in python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, colour=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    # list storing cubes
    body = []
    # key will represent current position of head
    # value will be set to the direction we turned
    turns = {}

    def __init__(self, colour, pos):
        self.colour = colour

        # head of snake
        self.head = Cube(pos)
        self.body.append(self.head)

        # x and y directions for moving the snake
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # var holds all key values
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    # direction by setting x and y coordinates
                    self.dirnx = -1
                    self.dirny = 0

                    # setting the value of turns to the direction of the head
                    self.turns[self.head.pos[:]] = [self.dirnx. self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0

                    self.turns[self.head.pos[:]] = [self.dirnx.self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1

                    self.turns[self.head.pos[:]] = [self.dirnx.self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1

                    self.turns[self.head.pos[:]] = [self.dirnx.self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]

            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])


    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    # size of the gap between vertical and horizontal lines on grid
    size_between = w // rows

    x, y = 0, 0
    for _ in range(rows):
        x += size_between
        y += size_between

        # draw the x and y grid lines
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global width, rows

    # filling the screen
    surface.fill((0, 0, 0))

    # drawing grid on window
    draw_grid(width, rows, surface)

    # updating display of window
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    # making width and rows global for referencing
    global width, rows

    # size for window
    width = 500

    # amount of rows which must divide into 500 evenly
    rows = 20

    # pygame window
    win = pygame.display.set_mode((width, width))

    # creating a snake object
    s = Snake((255, 0, 0), (10, 10))

    flag = True
    clock = pygame.time.Clock()

    # main program loop
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        # redrawing window everytime the loop iterates
        redraw_window(win)


main()
