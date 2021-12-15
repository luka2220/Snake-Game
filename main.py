# program for my snake game in python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, colour=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.colour = colour

    def move(self, dirnx, dirny):
        # changing the x, y directions for movement
        self.dirnx = dirnx
        self.dirny = dirny

        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        # distance between x, y values
        distance = self.w // self.rows

        row = self.pos[0]
        col = self.pos[1]

        # drawing a rectangle
        pygame.draw.rect(surface, self.colour, (row*distance+1, col*distance+1, distance-2, distance-2))

        # drawing eyes on snake
        if eyes:
            centre = distance // 2
            radius = 3

            circle_middle = (row * distance + centre-radius, col * distance + 8)
            circle_middle2 = (row * distance + distance - radius * 2, col * distance + 8)

            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


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
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # iterating through cube obj
        for i, c in enumerate(self.body):
            p = c.pos[:]  # grabbing position of the obj

            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])

                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                # will draw if it is the head of list(snake)
                c.draw(surface, True)
            else:
                c.draw(surface)


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
    global width, rows, s

    # filling the screen
    surface.fill((0, 0, 0))

    # displaying the snake
    s.draw(surface)

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
    global width, rows, s

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

        # will check if a key has been pressed every iteration
        s.move()

        # redrawing window everytime the loop iterates
        redraw_window(win)


main()
