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
    def __init__(self, colour, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    pass

def redraw_window(surface):
    pass

def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
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


main()
