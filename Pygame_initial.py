# import the pygame module, so you can use it
import pygame



# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("images/otherlogo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    #load another image in preparation for BLIT
    image = pygame.image.load("images/01_image.png")

    image.set_colorkey((255,0,255))

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240, 180))

    #background image
    background_image = pygame.image.load("images/background.png")
    screen.blit(background_image, (0, 0))


    #first BLIT
    screen.blit(image, (50, 50))

    #update screen
    pygame.display.flip()

    #screen.

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
