"""
    Let's plot color points on a surface, and blit it onto the screen?
"""

import sys
import pygame
import math
import cmath


def main():
    pygame.init()

    width = 1400
    height = 700
    screen = pygame.display.set_mode((width, height))

    dirty = True

    while 1:

        if dirty:
            screen.blit(screen, (0, 0, screen.get_width(), screen.get_height()))

            try:
                for j in range(height):
                    for i in range(width):
                        color = get_my_surface_color(width, height, i, j)
                        screen.set_at((i, j), color)
                    if j % 20 == 0:
                        pygame.display.update()
            except:
                print("an exception occurred")
        dirty = False
        # pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def colorize_screen_with_mandelbrot(screen):
    width = screen.get_width()
    height = screen.get_height()

    try:
        for j in range(height):
            for i in range(width):
                color = get_my_surface_color(width, height, i, j)
                screen.set_at((i, j), color)
                # instead of doing a 'screen.set_at()', how about setting pixels on a smaller surface
                # and blitting them onto the main screen? Say, break the main screen into a grid
                # having one surface that we re-use on each cell of the grid
            if j % 20 == 0:
                pygame.display.update()
    except:
        print("an exception occurred")


def mandelbrot(x, y, max_iterations) -> (int, bool):
    counter = 0
    mandelbrot_threshold = 2
    x_0 = x
    y_0 = y

    max_iterations = min(1000, max_iterations)

    while counter < max_iterations:
        x_1 = x_0 * x_0 - y_0 * y_0 + x
        y_1 = 2 * x_0 * y_0 + y
        x_0 = x_1
        y_0 = y_1
        counter += 1
        if x_1 * x_1 + y_1 * y_1 > mandelbrot_threshold:
            return counter, False

    return 0, True


def get_color_by_mandelbrot_layer(layer) -> (int, int, int):
    r = layer * 20 % 255
    g = (layer * 30 + 80) % 255
    b = (layer * 17 + 53) % 255
    return r, g, b


def get_my_surface_color(width, height, i, j):
    mandelbrot_width = 4
    mandelbrot_height = 2
    x = i * mandelbrot_width / width - mandelbrot_width / 2
    y = j * mandelbrot_height / height - mandelbrot_height / 2

    layer, is_mandelbrot = mandelbrot(x, y, 50)

    if is_mandelbrot:
        return 0, 0, 0
    else:
        return get_color_by_mandelbrot_layer(layer)  # (0, (j * 200 / height) + 55, (i * 200 / width) + 55)


if __name__ == '__main__':
    main()
