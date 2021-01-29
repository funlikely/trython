import sys
import pygame
import random
import math


def draw_graphical_grid(screen, color_offset):
    width = screen.get_rect().width
    height = screen.get_rect().height
    resolution = 33
    #
    # for i in range(0, width - width % 100, 100):
    #     for j in range(0, height - height % 100, 100):
    #         rect_color = get_little_rect_color(color_offset, i, j)
    #         pygame.draw.rect(screen, rect_color, (i, j, 90, 90))

    small_rect_width = width / resolution
    small_rect_height = height / resolution
    for i in range(0, resolution):
        for j in range(0, resolution):
            rect_color = get_little_rect_color(color_offset, i * 100, j * 100)
            pygame.draw.rect(screen, rect_color,
                             (i * width / resolution, j * height / resolution, small_rect_width, small_rect_height))


def get_little_rect_color(color_offset: float, i: int, j: int) -> (int, int, int):
    if (i + j) / 100 % 2 == 0:
        red_value = (255 - 20 * i / 100 + color_offset) % 256
        green_value = (128 - 10 * j / 100) % 256
        blue_value = (255 - color_offset) % 256
    else:
        red_value = (128 - 10 * j / 100 - color_offset) % 256
        green_value = 128
        blue_value = (255 - 20 * i / 100 - color_offset) % 256
    rect_color = (red_value, green_value, blue_value)
    return rect_color


def main():
    pygame.init()

    size = width, height = 960, 720
    my_face_speed = 2
    my_face_direction = math.pi / 4

    my_face_speed_x = math.cos(my_face_direction) * my_face_speed
    my_face_speed_y = math.sin(my_face_direction) * my_face_speed

    my_face_x_accumulator = 0
    my_face_y_accumulator = 0

    time_count = 0

    screen = pygame.display.set_mode(size)

    my_face_image = pygame.image.load("images/dogface.png")  # .convert()
    my_face_rect = my_face_image.get_rect()

    corn_face_image = pygame.image.load("images/catface.png")
    corn_face_rect = corn_face_image.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        my_face_x_accumulator += my_face_speed_x
        my_face_y_accumulator += my_face_speed_y

        my_face_rect = my_face_rect.move(my_face_x_accumulator, my_face_y_accumulator)

        my_face_x_accumulator, my_face_y_accumulator = reduce_coordinate_accumulators(my_face_x_accumulator,
                                                                                      my_face_y_accumulator)

        my_face_speed_x, my_face_speed_y = check_for_border_collision(width, height, my_face_rect, my_face_speed_x, my_face_speed_y)

        fill_color = (0, 0, 0)  # get_screen_fill_color(time_count)
        screen.fill(fill_color)
        draw_graphical_grid(screen, time_count)
        time_count += 1

        screen.blit(my_face_image, my_face_rect)
        pygame.display.flip()


def reduce_coordinate_accumulators(my_face_x_accumulator, my_face_y_accumulator):
    if my_face_x_accumulator >= 1:
        my_face_x_accumulator %= 1
    if my_face_y_accumulator >= 1:
        my_face_y_accumulator %= 1
    if my_face_x_accumulator <= -1:
        my_face_x_accumulator = (my_face_x_accumulator % 1) - 1
    if my_face_y_accumulator <= -1:
        my_face_y_accumulator = (my_face_y_accumulator % 1) - 1
    return my_face_x_accumulator, my_face_y_accumulator


def check_for_border_collision(width: int, height: int, my_face_rect: pygame.Rect, my_face_speed_x: float, my_face_speed_y: float) -> (float, float):
    if (my_face_rect.left < 0 and my_face_speed_x < 0) or (my_face_rect.right > width and my_face_speed_x > 0):
        my_face_speed_x = -1.0 * my_face_speed_x
    if (my_face_rect.top < 0 and my_face_speed_y < 0) or (my_face_rect.bottom > height and my_face_speed_y > 0):
        my_face_speed_y = -1.0 * my_face_speed_y
    return my_face_speed_x, my_face_speed_y


def get_screen_fill_color(time_count):
    red_value = (time_count / 13) % 256
    green_value = (128 - time_count / 7) % 256
    blue_value = (64 + time_count / 10) % 256
    fill_color = (red_value, green_value, blue_value)
    return fill_color


if __name__ == "__main__":
    main()
