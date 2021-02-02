"""
    Draw a Mandelbrot set

    TODO - Use threading to process blocks on the screen in parallel -- it is not working right. can't pickle a surface
    TODO - Figure out why the program freezes during rendering sometimes - possibly try reusing the block-sized
           pygame.Surface returned by create_mandelbrot_block()
    TODO - Find some pizza and eat it
    TODO - Improve color schemes

"""
from pygame.locals import *
import sys
import pygame
import math

# from multiprocessing import Pool


def create_mandelbrot_block(mandelbrot_size, mandelbrot_corner, screen_size, block_size, block_start):
    iterations_limit = 350

    surf = pygame.Surface(block_size)

    for i in range(surf.get_width()):
        for j in range(surf.get_height()):
            x = (i + block_start[0]) / screen_size[0] * mandelbrot_size[0] + mandelbrot_corner[0]
            y = (j + block_start[1]) / screen_size[1] * mandelbrot_size[1] + mandelbrot_corner[1]
            c = x + y * 1j

            layer, is_mandelbrot = mandelbrot_complex(c, iterations_limit)

            if is_mandelbrot:
                color = 0, 0, 0
            else:
                # there has to be a way with abs() and % to make it so these RGB values don't go from 255
                # down to 0, but instead bounce continuously between 0 and 255
                r = layer * 5 % 255
                g = (layer * 7 + 80) % 255
                b = (layer * 11 + 53) % 255
                color = r, g, b

            surf.set_at((i, j), color)

    return surf


def main():
    pygame.init()

    # screen_size = (1600, 960) # big and cool
    screen_size = (600, 360)  # small and for testing
    screen = pygame.display.set_mode(screen_size)

    block_size = (100, 80)

    # initial coordinate window information. will be updated by click-zooming during the application
    mandelbrot_size = (4, 2.4)
#    mandelbrot_center = (-0.5, 0)
    mandelbrot_corner = (-2.5, -1.2)
    time_count = 0

    zoom_factor = 10

    redraw = True

    while True:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # TODO: the math only work when zoom_factor = 2. Need to make it work for other values.
                    old_mandelbrot_size = mandelbrot_size
                    old_mandelbrot_corner = mandelbrot_corner

                    clicked_x = event.pos[0] / screen_size[0] * mandelbrot_size[0] + mandelbrot_corner[0]
                    clicked_y = event.pos[1] / screen_size[1] * mandelbrot_size[1] + mandelbrot_corner[1]

                    mandelbrot_size = (mandelbrot_size[0] / zoom_factor, mandelbrot_size[1] / zoom_factor)
                    mandelbrot_corner = ((clicked_x - mandelbrot_size[0] / 2), (clicked_y - mandelbrot_size[1] / 2))

                    print("old size " + str(old_mandelbrot_size) + ", new size " + str(mandelbrot_size) + ", old corner " + str(old_mandelbrot_corner) + ", new corner " + str(mandelbrot_corner))
                    redraw = True

        screen.blit(screen, (0, 0, screen.get_width(), screen.get_height()))

        # p = Pool()

        pixel_count = 0

        if redraw:
            # data = []
            for j in range(1, screen_size[1], block_size[1]):
                for i in range(1, screen_size[0], block_size[0]):
                    mandelbrot_block = create_mandelbrot_block(mandelbrot_size, mandelbrot_corner, screen_size,
                                                               block_size, (i, j))
                    screen.blit(mandelbrot_block, (i, j))
                    pygame.display.update()

                    pixel_count += block_size[0] * block_size[1]
                    # print("drew up " + str(pixel_count) + " pixels thus far")
            redraw = False

        time_count += 1
        pygame.display.update()


# this one uses complex numbers
def mandelbrot_complex(c, max_iterations) -> (int, bool):
    mandelbrot_threshold = 2
    z = 0 + 0j
    x = c.real
    y = c.imag
    y2 = y * y
    q = (x - 0.25) ** 2 + y2
    max_iterations = min(1000, max_iterations)

    if not (q * (q + (x - 0.25)) < y2 / 4.0 or (x + 1.0) ** 2 + y2 < 0.0625):
        for i in range(max_iterations):
            z = z ** 2 + c
            if abs(z) > mandelbrot_threshold:
                return i, False
    return 0, True


def mandelbrot(x, y, max_iterations) -> (int, bool):
    counter = 0

    # Need a good value for generating the borders on a mandelbrot picture
    mandelbrot_threshold = 3 * math.sqrt(2)

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


def get_my_surface_color(width, height, i, j):
    mandelbrot_width = 4
    mandelbrot_height = 2
    x = i * mandelbrot_width / width - mandelbrot_width / 2
    y = j * mandelbrot_height / height - mandelbrot_height / 2

    layer, is_mandelbrot = mandelbrot(x, y, 50)

    if is_mandelbrot:
        return 0, 0, 0
    else:
        r = layer * 20 % 255
        g = (layer * 30 + 80) % 255
        b = (layer * 17 + 53) % 255
        result = r, g, b
        return result  # (0, (j * 200 / height) + 55, (i * 200 / width) + 55)


if __name__ == '__main__':
    main()
