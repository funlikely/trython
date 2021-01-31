"""
    Let's plot color points on a surface, and blit it onto the screen?
"""

import sys
import pygame
import math
import cmath


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 400))

    # colorize_screen()
    colorize_screen_with_mandelbrot(screen)

    # screen.blit(screen, (0, 0, 900, 900))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def colorize_screen(screen):
    width = screen.get_width()
    height = screen.get_height()

    # my_surface = pygame.Surface(900, 900)
    for i in range(width):
        for j in range(height):
            screen.set_at((i, j), ((i * 255 / width), (j * 255 / height), 0))


def colorize_screen_with_mandelbrot(screen):
    width = screen.get_width()
    height = screen.get_height()


    for i in range(width):
        for j in range(height):
            color = get_my_surface_color(width, height, i, j)
            screen.set_at((i, j), color)


def mandelbrot(x, y, iteration_count) -> bool:
    x_0 = x
    y_0 = y

    iteration_count = min(1000, iteration_count)

    while iteration_count > 0:
        x_1 = x_0 * x_0 - y_0 * y_0 + x
        y_1 = 2 * x_0 * y_0 + y
        x_0 = x_1
        y_0 = y_1
        iteration_count -= 1
        if x_1 * x_1 + y_1 * y_1 > 16:
            return False

    return True


def get_my_surface_color(width, height, i, j):
    mandelbrot_width = 4
    mandelbrot_height = 2
    x = i * mandelbrot_width / width - mandelbrot_width / 2
    y = j * mandelbrot_height / height - mandelbrot_height / 2

    if mandelbrot(x, y, 50) == True:
        return (0, 0, 0)
    else:
        return ((i * 255 / width), (j * 255 / height), 0)


if __name__ == '__main__':
    main()
