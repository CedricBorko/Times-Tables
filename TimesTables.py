import random
import os
import pygame as pg
import numpy as np
import math


pg.init()
numPoints = 200
radius = 350
factor = 51
width, height = 1280, 1080
increment = 0.1
fullscreen = True
runningAnimation = False
window = pg.display.set_mode((width, height), pg.FULLSCREEN)
pg.display.set_caption('Times Tables')
colorDir = [True, False, True]
red, green, blue = random.randint(0, 125), random.randint(125, 255), 125
color = (red, green, blue)
speed = 10


def colorLoop():
    global red, green, blue, colorDir
    if colorDir[0]:
        if red < 255:
            red = red + 1
        else:
            colorDir[0] = False
    else:
        if red > 25:
            red = red - 1
        else:
            colorDir[0] = True
    if colorDir[1]:
        if green < 255:
            green = green + 1
        else:
            colorDir[1] = False
    else:
        if green > 25:
            green = green - 1
        else:
            colorDir[1] = True
    if colorDir[2]:
        if blue < 255:
            blue = blue + 1
        else:
            colorDir[2] = False
    else:
        if blue > 25:
            blue = blue - 1
        else:
            colorDir[2] = True


def setup():
    global factor, colorDir, red, green, blue, color, speed, increment
    factor = 0
    increment = 0.1
    colorDir = [True, False, True]
    red, green, blue = 237, 185, 43
    color = (red, green, blue)
    speed = 15


setup()
clock = pg.time.Clock()
run = True
while run:

    clock.tick(50 - 2 * speed - 2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_RIGHT]:
                numPoints += 10
            if pg.key.get_pressed()[pg.K_LEFT]:
                if numPoints > 10:
                    numPoints -= 10
            if pg.key.get_pressed()[pg.K_UP]:
                increment = 0.1
                if factor > 200:
                    increment = -0.1
            if pg.key.get_pressed()[pg.K_DOWN]:
                increment = -0.1
                if factor < 0:
                    increment = 0.1
            if pg.key.get_pressed()[pg.K_SPACE]:
                runningAnimation = not runningAnimation
                factor = round(factor, 1)
            if pg.key.get_pressed()[pg.K_2]:
                if not runningAnimation:
                    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            if pg.key.get_pressed()[pg.K_1]:
                setup()
            if pg.key.get_pressed()[pg.K_a]:
                if speed < 20:
                    speed += 1

            if pg.key.get_pressed()[pg.K_d]:
                if speed > 1:
                    speed -= 1
            if pg.key.get_pressed()[pg.K_F11]:
                if not fullscreen:
                    width, height = 1920, 1080
                    window = pg.display.set_mode((width, height), pg.FULLSCREEN)
                    fullscreen = True
                else:
                    width, height = 1280, 1000
                    pg.display.quit()
                    pg.display.init()
                    window = pg.display.set_mode((width, height))
                    fullscreen = False
            if pg.key.get_pressed()[pg.K_ESCAPE]:
                if fullscreen:
                    width, height = 1280, 1000
                    pg.display.quit()
                    pg.display.init()
                    window = pg.display.set_mode((width, height))
                    fullscreen = False
            if pg.key.get_pressed()[pg.K_3]:
                if not runningAnimation:
                    pg.image.save(window, "C:/Users/Cedric/Desktop/screenshot.jpg")


    pg.draw.rect(window, (0, 0, 0), (0, 0, width, height))

    if runningAnimation:
        factor += increment / speed
        factor = float("{0:1f}".format(factor))
        colorLoop()
        color = (red, green, blue)

    pg.draw.circle(window, color, (width // 2, - radius // 4 + height // 2), radius, 1)

    for i in np.arange(0, 2 * 3.14159265359, 3.14159265359 / (numPoints // 2)):
        x = width // 2 + radius * math.cos(i)
        y = - radius // 4 + height // 2 + radius * math.sin(i)
        lineP1 = (x, y)
        lineP2 = (width / 2 + radius * math.cos(factor * i),
                  - radius // 4 + height / 2 + radius * math.sin(factor * i))
        pg.draw.line(window, color, lineP1, lineP2, 1)

    pg.draw.line(window, (255, 255, 255), (0, 4 / 5 * height), (width, 4 / 5 * height), 5)

    pg.font.init()
    font = pg.font.SysFont('Comic Sans MS', 40)
    if factor < 100:
        factorS = '{0:.3g}'.format(factor)
    elif factor < 10:
        factorS = '{0:.2g}'.format(factor)
    else:
        factorS = '{0:.4g}'.format(factor)
    text1 = font.render(f'Factor: {factorS}', False, (255, 255, 255))
    text2 = font.render(f'Number of Points: {numPoints}', False, (255, 255, 255))
    text3 = font.render(f'Animation speed: {21 - speed}', False, (255, 255, 255))

    window.blit(text1, (width / 2 - 100, 4 / 5 * height + 20))
    window.blit(text2, (width / 2 - 215, 4 / 5 * height + 70))
    window.blit(text3, (width / 2 - 180, 4 / 5 * height + 120))

    pg.display.update()
