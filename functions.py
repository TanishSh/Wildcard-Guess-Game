# importing different libraries and files
# imports the globals.py where there are some global variables declared
import globals
#imports pygame (graphics library), random, and pygame_textinput (to get text input from users in pygame)
import pygame
import random
import pygame_textinput

# user-defined function to load an image by using the pygame.image.load(), where we have to give the filepath of the image
#param: location: filpath of the image
def imageLoad(location):
    pic = pygame.image.load(location)
    return pic

#user-defined function to render text using the font.render(), and returns the text along with the rectangle that is created while we show texts in pygame
#param: text: 
#param: font:
#param: color: the color of the text in rgb or any other valid format
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#user-defined function to create responsive and functional buttons
#param: message: the text in the button
#param: x: x coordinate of the button, which is the top left-hand side of the button
#param: y: y coordinate of the button, which is the top left-hand side of the button
#param: width: the width of the button in px
#param: height: the height of the button in px
#param: textSize: font size of the message in the button
#param: activeColor: color to show when mouse hovers over the button
#param: inactiveColor: color to show when mouse is not on top or does not hover over the button
#param: action: asks an object of a function to be passed and then executes it by calling it as a function
############## enables to change state of the game (intro, instructions, game, end), by passing in the object (like intro), 
############## which takes us back to that state (like takes us back again to intro of the game)
def button(message, x, y, width, height, textSize, activeColor, inactiveColor, action=None):
    # event that gets the position of the mouse on the pygame screen
    mouse = pygame.mouse.get_pos()

    # event that gets when the user clicks
    click = pygame.mouse.get_pressed()

    # if mouse is in between in the x and y coordinate
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        # it means the mouse is hovering over the button
        # so the button would show it's active color
        # so we draw a new rectangle (button) with the active color, to give the illusion that the button is changing colors
        pygame.draw.rect(globals.screen, activeColor, (x, y, width, height))
        # a click has occured
        # this action is check for the game, which returns a one, which triggers the checking inside the main game function
        if click[0] == 1 and action == 'check':
            return 1
        # if the button is clicked and it has a action, perform the action
        elif click[0] == 1 and action != None:
            action()
    else:
        # just draw the button with it's inactive color sine the mouse is not hovering over the button
        pygame.draw.rect(globals.screen, inactiveColor, (x, y, width, height))

    # for the text inside the button
    text = pygame.font.Font('fonts/FiraSans-ExtraBoldItalic.ttf', textSize)
    TextSurf, TextRect = text_objects(message, text, globals.white)
    # centers the text inside the button
    TextRect.center = ((x+(width/2)),(y+(height/2)))
    globals.screen.blit(TextSurf, TextRect)

# code for background animation
# param: option: 1 or 2: 1 is if we want animation with the poker card pictures (such as in the intro)
######################## 2 is if we want animation with sqares (such as in the transition in the game, when the user gets the right name of the card)
def backgroundAnimation(option):
    #counter for the x to keep track of odd and even increments
    #so that the black and white images can alternate
    # and we do not have same colored picture side by side
    counterX = 1
    # to load and initialize the images in the variables
    background1 = imageLoad('images/cards1.png')
    background2 = imageLoad('images/cards2.png')
    # loop to get the animation
    # increment values for y and x achieved through trial and error
    # the jist for the increment values is that it resembles the spacing of the background1 and background2 in px in both x and y
    # so that they never overlap over each other... it is a nice neat animation with all pictures side by side
    for y in range(0, globals.height+1, 69):
        for x in range(0, globals.width+1, 55):
            # a variable that randomly picks between 0 and 1
            # it has a purpose, we want to randomly choose (0 or 1) if the picture should show up in the canvas/display/screen or not
            # this creates a dynamic animation
            probability = random.randint(0,1)
            if counterX % 2 == 0:
                if probability:
                    if(option == 1):
                        globals.screen.blit(background2,[x,y])
                    elif(option == 2):
                        box(x,y,15,15,globals.red)
            else:
                if probability:
                    if(option == 1):
                        globals.screen.blit(background1,[x,y])
                    elif(option == 2):
                        box(x,y,15,15,globals.violet)
            # counter increments
            counterX = counterX + 1
            
# used to display header text inside container box
# param: writing: the text that the header will display
# param: boxWidth: the width of the container
# param: boxHeight: the height of the container
# param: size: the size of the container
def boxTextTitle(writing, boxWidth, boxHeight, size):
    text = pygame.font.Font('fonts/Lobster-Regular.ttf', size)
    TextSurf, TextRect = text_objects(writing, text, globals.lightBlue)
    TextRect.center = ((boxWidth/2),(boxHeight/2-150))
    globals.screen.blit(TextSurf, TextRect)

# used to make a box or container
# param: x: the x coordinate
# param: y: the y coordinate
# param: width: the width
# param: height: the height
# param: color: the color
def box(x, y, width, height, color):
    pygame.draw.rect(globals.screen, color, pygame.Rect(x,y,width,height))
   
# used to render text
# param: style: the font style or type
# param: size: the size of the font
def text(style, size, writing, color, x, y):
    font = pygame.font.Font(style, size)
    text = font.render(writing, True, color)
    globals.screen.blit(text, (x, y))

# used to show how many seconds is left (works like a second clock)
# param: seconds: the no. of seconds to show (range - 0 to 59)
def timer(seconds, x, y):
    outputTime = "time: {}s".format(seconds)
    text(None, 35, outputTime, globals.blue, x, y)

# used to create boundary or outline in the display screen
# each of the first 4 params represent the corners of the outline (think it of as a corner of a sqare or rectangle)
#param: thickness: the line thickness
def boundary(topLeftCorner, topRightCorner, bottomLeftCorner, bottomRightCorner, thickness):
    pygame.draw.line(globals.screen, globals.brown, topLeftCorner, topRightCorner, thickness)
    pygame.draw.line(globals.screen, globals.brown, topRightCorner, bottomRightCorner, thickness)
    pygame.draw.line(globals.screen, globals.brown, topLeftCorner, bottomLeftCorner, thickness)
    pygame.draw.line(globals.screen, globals.brown, bottomLeftCorner, bottomRightCorner, thickness)
            
# used to scale pictures to make all pictures to be unified in terms of dimension
def scale(pictureLocation):
    width = 500
    height = 250
    backgroundPic = imageLoad(pictureLocation)
    scaledPic = pygame.transform.scale(backgroundPic, (width,height))
    return scaledPic

# used to check pygame event queue to see if the user wants to exit the program
def events():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# used to make a transparent container or box
# param: alpha: the transparency level of the color of the box
def alphaBox(x, y, width, height, alpha, boxColor):
    s = pygame.Surface((width,height))
    s.set_alpha(alpha)
    s.fill(boxColor)
    globals.screen.blit(s,(x,y))
   
# used to show the text in the hint box
def hint(writing, size, boxWidth, boxHeight, color, header=0):
    text = pygame.font.Font('fonts/FiraSans-Regular.ttf', size)
    TextSurf, TextRect = text_objects(writing, text, color)
    if (header == 1):
        TextRect.center = ((boxWidth/2),(boxHeight/2+80))
    elif(header == 0):
        TextRect.center = ((boxWidth/2),(boxHeight/2+120))

    if (TextRect[0] <= 0):
        TextRect[0] = 25
    globals.screen.blit(TextSurf, TextRect)













