import pygame
import functions
import pygame_textinput
import globals
import random

# lists to store pictures , answers, and hints for each level, and the text transitions between each level
pictures = ['images/google.jpg','images/dog.jpg','images/monaLisa.jpg','images/kid.jpg','images/santa.jpg','images/ironman.jfif', 'images/spongebob.jpg', 'images/napoleon.jpg','images/beatles.jpg', 'images/michaelJackson.jpg']
answers = ['google','dog','monalisa','kid', 'santa', 'ironman', 'spongebob', 'napoleon', 'beatles', 'michaeljackson']
hints = [['Most popular search engine', 'One of the tech giants', 'Founders - Larry and Sergy'], ['An animal', "A man's best friend", 'Domesticated Mammal'], ['A famous painting', 'Painted by Leonardo da Vinci', 'Art Masterpiece'], ['Synonym for child?', 'Synonym for baby?', 'Three letter word'], ['Kids are most excited about him', '5 letter word', 'Think about Christmas'], ['A marvel comic hero', 'He is made of iron', 'Tonay Stark is his name'], ["A kid's cartoon show", 'He is sponge', 'Last three letters are - bob'], ['Related to French Revolution', 'A French Emperor', 'French Statesman'], ['English Rock Band', 'Most influential band in 1960s', 'Name of an insect?'], ['King of Pop Music', 'Creator of the song "Beat it"', 'First Name is Michael']]
transition = ['Great Job!', 'Way to GO!', 'Wow!', 'Nice!', 'Wonderful!', 'Keeping Going!', 'You will get there :)', 'Keeping Working Hard!', 'You are almost there!', 'Bravo! :)']

#scale the pictures
for i, picture in enumerate(pictures):
    scaledPicture = functions.scale(picture)
    pictures[i] = scaledPicture

#if all the levels are complete or the time runs out
#param: state: 1 or 0
############# 1 means all 10 levels successfully complete
############# 0 means time ran before all levels were completed
#param: level: the level of the user
def endDialogueBox(state, level):
    if(state == 1):
        display = "Great Job!"
    elif(state == 0):
        display = "Time's UP! Better Luck Next Time :)"
    score = level
    while(True):
        #check for quit event
        functions.events()
        # 30 fps
        globals.clock.tick(30)
        globals.screen.fill(globals.black)
        # draws a white box
        functions.box(((globals.width/2)-650/2), ((globals.height/2)-500/2), 650, 500, globals.white)
        # shows the text which is stored in the display variable
        text = pygame.font.Font('fonts/FiraSans-Regular.ttf', 40)
        TextSurf, TextRect = functions.text_objects(display, text, globals.lightBlue)
        TextRect.center = ((800/2),(350/2-100))
        globals.screen.blit(TextSurf, TextRect)
        # shows the score
        TextSurf, TextRect = functions.text_objects('Your Score is ' + str(score) + ' / 10', text, globals.lightBlue)
        TextRect.center = ((800/2),(350/2))
        globals.screen.blit(TextSurf, TextRect)

        text = pygame.font.Font('fonts/FiraSans-Regular.ttf', 30)
        TextSurf, TextRect = functions.text_objects('What would you like to do now?:', text, globals.lightBlue)
        TextRect.center = ((800/2),(350/2+70))
        globals.screen.blit(TextSurf, TextRect)
        # different buttons
        functions.button('Play Again',(globals.width/2-200/2),((globals.height/2)-(50/2)+90), 200, 50, 30, globals.green, globals.blue, game)
        functions.button('Quit Game', (globals.width/2-200/2),((globals.height/2)-(50/2)+150), 200, 50, 30, globals.red, globals.blue, quit)
        functions.button('Home Menu', (globals.width/2-200/2),((globals.height/2)-(50/2)+210), 200, 50, 30, globals.violet, globals.blue, intro)
        pygame.display.flip()

def intro():
    pygame.display.set_caption("Wildcard Guess Game")
    icon = functions.imageLoad('images/card.png')
    pygame.display.set_icon(icon)
    intro = True
    while(intro):
        # 10 fps for the animation to run the best
        globals.clock.tick(10)
        functions.events()
        globals.screen.fill(globals.white)
        # animation
        functions.backgroundAnimation(1)
        # create a white box
        functions.box(((globals.width/2)-450/2),((globals.height/2)-400/2), 450, 400, globals.white)
        functions.boxTextTitle('Wildcard Guess Game', 800, 500, 50)
        # buttons
        functions.button('Start', 300, 250, 200, 50, 25, globals.green, globals.blue, instructions)
        functions.button('Exit', 300, 350, 200, 50, 25, globals.red, globals.blue, quit)
        pygame.display.flip()

def instructions():
    instruct = True
    while(instruct):
        # 30 fps
        globals.clock.tick(30)
        functions.events()
        # draw a white box
        functions.box(((globals.width/2)-800/2), ((globals.height/2)-500/2), 800, 500, globals.white)
        functions.boundary((10,10), (789,10), (10, 485), (789,485), 3)
        functions.boxTextTitle('Game Rules', 800, 500, 40)
        # intialize the bullet point
        bulletPoint = functions.imageLoad('images/dot.png')
        # keep drawing the bullet point before each game rules
        globals.screen.blit(bulletPoint, (25,150))
        globals.screen.blit(bulletPoint, (25,200))
        globals.screen.blit(bulletPoint, (25,250))
        globals.screen.blit(bulletPoint, (25,300))
        globals.screen.blit(bulletPoint, (25,350))
        # write the game rules
        functions.text('fonts/FiraSans-Regular.ttf', 18, 'There are 10 levels in the game', globals.lightBlue, 50, 150)
        functions.text('fonts/FiraSans-Regular.ttf', 18, 'In each successive level the time decrease by 2 seconds', globals.lightBlue, 50, 200)
        functions.text('fonts/FiraSans-Regular.ttf', 18, 'You have to answer within the given time, or the game ends and you get your score', globals.lightBlue, 50, 250)
        functions.text('fonts/FiraSans-Regular.ttf', 18, 'In each level, you are given a card (picture), and you have to guess the name of the card', globals.lightBlue, 50, 300)
        functions.text('fonts/FiraSans-Regular.ttf', 18, 'Hints are provided if you are repeatedly unsuccessful to guess the right name', globals.lightBlue, 50, 350)
        # buttons
        functions.button('Menu', 180, 410, 100, 50, 25, globals.violet, globals.blue, intro)
        functions.button('Quit', 350, 410, 100, 50, 25, globals.red, globals.blue, quit)
        functions.button('Play', 520, 410, 100, 50, 25, globals.green, globals.blue, game )
        pygame.display.flip()

def game():
    # zip all the list to make them a unified tuple based on their indexs
    mapped = list(zip(pictures, answers, hints, transition))
    # randomly order zipped tuples
    random.shuffle(mapped)
    # unzip them and store them in new variables
    picturesS, answersS, hintsS, transitionS = zip(*mapped)
    # run for 10 times because there are 10 levels
    for i in range(10):
        # instantiate the textinput object
        textinput = pygame_textinput.TextInput()
        frameCount = 0
        frameRate = 30
        count = 0
        # startTime aka the no. of seconds in each game decreases by 2 after the first level
        # the first level has 30 seconds
        startTime = 30 - ((i)*2)
        # to keep count of the no. of errors
        error = 0
        answered = False
        # until the player answers the name of the card correctly
        while(not answered):
            # 30 fps
            globals.clock.tick(30)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            globals.screen.fill(globals.white)
            # creates the beautiful brown outline boundaries in the screen around the edges and around the picture
            functions.boundary((15,20),(785,20),(15,480),(785,480),5)
            functions.boundary((15+15,20+15),(785-15,20+15),(15+15,480-15),(785-15,480-15),2)
            functions.boundary((105,60),(675,60),(105,375),(675,375),3)
            #shows text
            functions.text('fonts/FiraSans-BoldItalic.ttf', 40, "Guess What's the Name ?", globals.lightBlue, (globals.width/2)-240 , (globals.height/2)-200)
            functions.text('fonts/FiraSans-BoldItalic.ttf', 25, 'The Name of the Card is', globals.lightBlue, 35, 410)
            # the text box where the user has to type in the answer
            functions.box(((globals.width/2)-220/2+20), ((globals.height/2)-50/2+180), 290, 50, globals.gray)
            # updates the textinput
            textinput.update(events)
            # puts the cursor insde the gray text box
            globals.screen.blit(textinput.get_surface(),(((globals.width/2)-220/2+25),((globals.height/2)-50/2+185)))
            # shows the picture (card) to the player
            globals.screen.blit(picturesS[i], (140,100))
            # the check button
            check = functions.button('Check',640,((globals.height/2)-50/2+180), 120, 50, 25, globals.green, globals.blue, 'check')
            # if the player clicks the button
            if (check):
                # if the type in answer is the name of the card
                if(textinput.get_text().lower().replace(" ","") == answersS[i]):
                    # for the transition animation
                    while(count < 10):
                        for event in events:
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        globals.screen.fill(globals.white)
                        # animation with colorful squares
                        functions.backgroundAnimation(2)
                        # transition text
                        functions.boxTextTitle(transitionS[i], 800, 500, 80)
                        globals.clock.tick(10)
                        count+=1
                        pygame.display.flip()
                    # get the answered to be true
                    answered = True
                # if the type in answer is not he name of the card
                elif(textinput.get_text().lower().replace(" ","") != answersS[i]):
                    # let the player know about it by displaying text in red
                    functions.text('fonts/FiraSans-BoldItalic.ttf', 20, 'Try Again! That is not the name of the card', globals.red, ((globals.width/2)-220/2-80), ((globals.height/2)-50/2+150))
                    # attempting to count the no. of times the user makes a mistake
                    error += 1
          
            #decrement seconds as each second passes
            # a second is the frameCount // frameRate
            totalSeconds = startTime - (frameCount // frameRate)

            # if time runs out
            if (totalSeconds < 0):
                # end the game and move to the end dialogue box
                endDialogueBox(0, i)

            if totalSeconds < 0:
                totalSeconds = 0

            seconds = totalSeconds % 60
            # show the timer
            functions.timer(seconds,globals.width-130, 35)
            # show the level to the player
            functions.text('fonts/Lobster-Regular.ttf', 30, 'Level: ' +str(i + 1), globals.blue, 20 , 25)
            # error for some reason are in multiples of 4
            # i.e if the player makes error once, then the error value is incrmented by around 4 in average
            # so 16 is 4 errors, 12 is 3 errors, and 4 is 1 error in reality
            if(error > 16):
                functions.alphaBox(0, 100, 480, 100, 140, globals.green)
                functions.hint('HINT: ', 30, 480, 100, globals.blue, 1)
                functions.hint(hintsS[i][2], 30, 480, 100, globals.blue)

            elif(error > 12):
                functions.alphaBox(0, 100, 480, 100, 140, globals.green)
                functions.hint('HINT: ', 30, 480, 100, globals.blue, 1)
                functions.hint(hintsS[i][1], 30, 480, 100, globals.blue)
            
            elif(error > 4):
                functions.alphaBox(0, 100, 480, 100, 140, globals.green)
                functions.hint('HINT: ', 30, 480, 100, globals.blue, 1)
                functions.hint(hintsS[i][0], 30, 480, 100, globals.blue)
            #keep track of the frame count
            frameCount += 1
            pygame.display.flip()

    # if the player finishes the game
    endDialogueBox(1, 10)
    






    

    
