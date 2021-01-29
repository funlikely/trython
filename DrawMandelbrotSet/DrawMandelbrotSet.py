"""
    Let's plot color points on a surface, and blit it onto the screen?
"""

import sys
import pygame
import math
import cmath


def create_mandelbrot_block(mandelbrot_size, mandelbrot_center, screen_size, block_size, block_start) -> pygame.Surface:
    surf = pygame.Surface(block_size)

    scale_x = mandelbrot_size[0] / screen_size[0]
    scale_y = mandelbrot_size[1] / screen_size[1]

    screen_scoot_x = block_start[0]
    screen_scoot_y = block_start[1]

    for i in range(surf.get_width()):
        for j in range(surf.get_height()):
            scaled_down_x = (screen_scoot_x + i) / screen_size[0]
            scaled_up_x = scaled_down_x * mandelbrot_size[0]
            x = scaled_up_x - (mandelbrot_size[0]-mandelbrot_center[0]) / 2
            scaled_down_y = (screen_scoot_y + j) / screen_size[1]
            scaled_up_y = scaled_down_y * mandelbrot_size[1]
            y = scaled_up_y -(mandelbrot_size[1] - mandelbrot_center[1]) /2

            layer, is_mandelbrot = mandelbrot(x, y, 50)

            if is_mandelbrot:
                color =  0, 0, 0
            else:
                color =  get_color_by_mandelbrot_layer(layer)

            surf.set_at((i, j), color)

    return surf


def main():
    pygame.init()

    screen_size = (1600, 960)
    block_size = (100, 55)
    screen = pygame.display.set_mode(screen_size)

    mandelbrot_size = (4,2.4)
    mandelbrot_center = (-0.5,0)
    time_count = 0

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(screen, (0, 0, screen.get_width(), screen.get_height()))

        for j in range(1, screen_size[1], block_size[1]):
            for i in range(1, screen_size[0], block_size[0]):


                # surface_to_color = pygame.Surface((block_width, block_height))
                # surface_to_color.fill(((i*53 + j*7 + time_count) % 255, (i * 11 + j *17 + time_count/2) % 255, (i*23 + j*19 + time_count/3) % 255))

                mandelbrot_block = create_mandelbrot_block(mandelbrot_size, mandelbrot_center, screen_size, block_size, (i,j))

                screen.blit(mandelbrot_block, (i, j, i + block_size[0], j + block_size[1]))

                pygame.display.update()
                # color = get_my_surface_color(screen_width, screen_height, i, j)
                # screen.set_at((i, j), color)

        time_count +=1


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
