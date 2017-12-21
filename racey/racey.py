#!/usr/bin/python3

import pygame
import time


# initiate the module
pygame.init()

display_width = 800
display_height = 600

# set RBG color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# set window size
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Set title of windows
pygame.display.set_caption("A bit Racey")
# Game clock/ Time
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')


# cars functions
def car(x, y):
    # displaying car at x, y location
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont('Pagul', 115, True)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(TextSurf, TextRect)

    time.sleep(2)

    game_loop()


def crash():
    message_display('You crashed!')


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    car_width = 40
    x_change = 0

    # Variable for exiting the loop
    gameExit = False

    # Starting the game loop
    while not gameExit:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # This checks for key presses left and right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        # drawing white background
        gameDisplay.fill(white)
        # drawing car to the white background, order is relevant
        car(x, y)

        # logic handler "crash"
        if x > display_width - car_width or x < 0:
            crash()

        # could use pygame.display.flip() here
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
