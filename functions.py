import globals
import pygame
import random
import time

def imageLoad(location):
    pic = pygame.image.load(location)
    return pic

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(message, x, y, width, height, activeColor, inactiveColor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(globals.screen, activeColor, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(globals.screen, inactiveColor, (x, y, width, height))

    text = pygame.font.Font('fonts/FiraSans-ExtraBoldItalic.ttf', 25)
    TextSurf, TextRect = text_objects(message, text, globals.white)
    TextRect.center = ((x+(width/2)),(y+(height/2)))
    globals.screen.blit(TextSurf, TextRect)

def introBackgroundAnimation():
    counterX = 1
    background1 = imageLoad('images/cards1.png')
    background2 = imageLoad('images/cards2.png')
    for y in range(0, globals.height+1, 69):
        for x in range(0, globals.width+1, 55):
            probability = random.randint(0,1)
            if counterX % 2 == 0:
                if probability:
                    globals.screen.blit(background2,[x,y])
            else:
                if probability:
                    globals.screen.blit(background1,[x,y])
            counterX = counterX + 1
    pygame.time.delay(100)

def boxTextTitle(writing, boxWidth, boxHeight):
    text = pygame.font.Font('fonts/Lobster-Regular.ttf', 50)
    TextSurf, TextRect = text_objects(writing, text, globals.black)
    TextRect.center = ((boxWidth/2),(boxHeight/2-150))
    globals.screen.blit(TextSurf, TextRect)

def box(x, y, width, height, color):
    pygame.draw.rect(globals.screen, color, pygame.Rect(x,y,width,height))

def intro():
    pygame.display.set_caption("Wildcard Guess Game")
    icon = imageLoad('images/card.png')
    pygame.display.set_icon(icon)
    intro = True
    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        globals.screen.fill(globals.white)
        introBackgroundAnimation()
        box(((globals.width/2)-450/2),((globals.height/2)-400/2), 450, 400, globals.white)
        boxTextTitle('Wildcard Guess Game', 800, 500)
        mouse = pygame.mouse.get_pos()
        button('Start', 300, 250, 200, 50, globals.green, globals.black, instructions)
        button('Exit', 300, 350, 200, 50, globals.red, globals.black, quit)
        pygame.display.flip()

def instructions():
    print("hello")
    instruct = True
    while(instruct):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        globals.screen.fill(globals.black)
        box(((globals.width/2)-600/2), ((globals.height/2)-450/2), 600, 450, globals.white)
        boxTextTitle('Game Rules', 800, 500)
        button('Menu', 180, 410, 100, 50, globals.violet, globals.black, intro)
        button('Quit', 350, 410, 100, 50, globals.red, globals.black, quit)
        button('Play', 520, 410, 100, 50, globals.green, globals.black, game )
        pygame.display.flip()


def game():
    print("game")
    game = True
    while(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        globals.screen.fill(globals.black)
        box(((globals.width/2)-400/2), ((globals.height/2)-250/2), 400, 250, globals.white)
        pygame.display.flip()
