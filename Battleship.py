import pygame
import time
import random
import os
import sys
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (4, 229, 225)
ORANGE = (249, 141, 0)
BLUE = (0, 73, 209)
DARKBLUE = (0,0,128)
GREY = (122,122,122)

    #more "specific" colors. 
OCEAN = (7,87,91)
WAVE = (102,165,173)
SEA = (47,73,110)
BISCOTI = (235,181,130)
 
pygame.init()

#start the music
try:
    pygame.mixer.music.load('PacificRimTheme.mp3')
    pygame.mixer.music.play(-1)
except Exception:
    nothing = "nothing"

# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Battleship")
 
# Loop until the user clicks the close button.
done = False
end = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#--- title screen setup ---
themenumber = 1
titlescreenshipsX = [27, 67, 107, 147, 187, 147, 187, 227, 267, 67, 67, 67, 307, 347, 387, 147, 147]
titlescreenshipsY = [392, 392, 392, 392, 392, 432, 432, 432, 432, 112, 152, 192, 272, 272, 272, 312, 272]
backgroundcolor = BLUE
gridcolor = DARKBLUE
titlegridX = []
titlegridY = []
compselectionboxX = 464
theme1outline = RED
theme2outline = WHITE
theme3outline = WHITE
theme4outline = WHITE
theme5outline = WHITE
theme6outline = WHITE
gamehelp = False
   
#--- player setup ---
shipchoice = 1
placershiplen = 5
placemode = True
gridX = []
gridY = []
playershipsX = []
playershipsY = []
shipprogress = 0
finalshipplacement = False
finalshipplacementX = 0
finalshipplacementY = 0
orientation = "none"
selectposition = False
PlacementColor = GREY
directionchosen = False
computer = "off"
listchoiceX = playershipsX
listchoiceY = playershipsY

#--- computer setup ---
computerplacing = True
compshipsX = []
compshipsY = []
directions = []
computerplacing = True
emptyspace = False
restofcomputership = False
directionfalse = False

#--- setup for loops ---
#this loop sets up the main game grid
currentgridX = 25
currentgridY = 25
for i in range(10):
    for i in range(10):
        gridX.append(currentgridX)
        gridY.append(currentgridY)
        currentgridX+=45
    currentgridX = 25
    currentgridY += 45
#this loop sets up the title screen grid
currentgridX = 25
currentgridY = 70
for i in range(10):
    for i in range(10):
        titlegridX.append(currentgridX)
        titlegridY.append(currentgridY)
        currentgridX+=40
    currentgridX = 25
    currentgridY += 40

#--- Main Game setup ---
playershotsX = []
playershotsY = []
playershotcolor = []
compshotsX = []
compshotsY = []
compshotcolor = []
turn = "player 1"
playerhits = 0
comphits = 0
hit = False
alreadyshot = False
compalreadyshot = True
search_and_destroy = False
compshootdirection = "none"
sunkID = 0
sunkList = []
sunkListStrings = []

# -------- Title Screen Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            end = True

    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
                if computer == "on":
                    computer = "off"
                    compselectionboxX = 435
            elif event.key == pygame.K_RIGHT:
                if computer == "off":
                    computer = "on"
                    compselectionboxX = 463
            elif event.key == pygame.K_UP:
                if themenumber > 1:
                    themenumber-=1
            elif event.key == pygame.K_DOWN:
                if themenumber < 6:
                    themenumber+=1
           
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(backgroundcolor)

    #Mouse detection
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        
    # --- Game logic should go here
    theme1outline, theme2outline, theme3outline, theme4outline, theme5outline, theme6outline = WHITE, WHITE, WHITE, WHITE, WHITE, WHITE 
    if themenumber == 1:
        backgroundcolor = BLUE
        gridcolor = DARKBLUE
        theme1outline = RED
    elif themenumber == 2:
        backgroundcolor = DARKBLUE
        gridcolor = BLACK
        theme2outline = RED
    elif themenumber == 3:
        backgroundcolor = DARKBLUE
        gridcolor = GREEN
        theme3outline = RED
    elif themenumber == 4:
        backgroundcolor = BLACK
        gridcolor = DARKBLUE
        theme4outline = RED
    elif themenumber == 5:
        backgroundcolor = OCEAN
        gridcolor = WAVE
        theme5outline = RED
    elif themenumber == 6:
        backgroundcolor = SEA
        gridcolor = BISCOTI
        theme6outline = RED

    if pressed1:
        if (mouseX >=435) and (mouseX <=493) and (mouseY >= 400) and (mouseY <= 458):
            done = True
        elif (mouseX >=435) and (mouseX <=493) and (mouseY >= 330) and (mouseY <= 388):
            helpdone = False
            while helpdone ==  False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        helpdone = True
                if (mouseX >=190) and (mouseX <=310) and (mouseY >= 450) and (mouseY <= 485) and pressed1:
                    helpdone = True
                        
                screen.fill(backgroundcolor)

                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

                #I used "helptext" as a variable over and over again in the interest of not having other variables. The code just changes the variable for each new line and prints it
                helptitlefont = pygame.font.SysFont('Calibri', 24, True, False)
                helpbodyfont = pygame.font.SysFont('Calibri', 16, True, False)
                helptext = helptitlefont.render("For the Title Screen:",True,WHITE)
                screen.blit(helptext, [10, 5])
                helptext = helpbodyfont.render("Use the LEFT and RIGHT arrow keys to turn the computer player on and",True,WHITE)
                screen.blit(helptext, [10, 35])
                helptext = helpbodyfont.render("off (if the computer player is off, a second human player can play).",True,WHITE)
                screen.blit(helptext, [10, 50])
                helptext = helpbodyfont.render("The UP and DOWN keys change the theme (coloring) of the game.",True,WHITE)
                screen.blit(helptext, [10, 75])
                helptext = helpbodyfont.render("Once you have all the settings you want, hit 'GO!' to start the game.",True,WHITE)
                screen.blit(helptext, [10, 100])
                helptext = helptitlefont.render("For Setup:",True,WHITE)
                screen.blit(helptext, [10, 125])
                helptext = helpbodyfont.render("Each side has 5 ships: An Aircraft Carrier (5 spaces), a Battleship",True,WHITE)
                screen.blit(helptext, [10, 155])
                helptext = helpbodyfont.render("(4 spaces), a Destroyer (3 spaces), a Submarine (3 spaces) and a",True,WHITE)
                screen.blit(helptext, [10, 170])
                helptext = helpbodyfont.render("Patrol Boat (2 spaces).",True,WHITE)
                screen.blit(helptext, [10, 185])
                helptext = helpbodyfont.render("For each ship:",True,WHITE)
                screen.blit(helptext, [10, 210])
                helptext = helpbodyfont.render("1) Click a square to place an end of that ship. (press backspace to undo)",True,WHITE)
                screen.blit(helptext, [10, 225])
                helptext = helpbodyfont.render("2) Use the arrow keys to choose the direction it's pointed in",True,WHITE)
                screen.blit(helptext, [10, 240])
                helptext = helpbodyfont.render("3) Press shift to finalize its position and move on to the next ship",True,WHITE)
                screen.blit(helptext, [10, 255])
                helptext = helpbodyfont.render("NOTE: If there are two players, the setup will switch immediatly from",True,WHITE)
                screen.blit(helptext, [10, 280])
                helptext = helpbodyfont.render("the first player's Patrol Boat to the second player's Aircraft Carrier",True,WHITE)
                screen.blit(helptext, [10, 295])
                helptext = helptitlefont.render("For GamePlay:",True,WHITE)
                screen.blit(helptext, [10, 320])
                helptext = helpbodyfont.render("Once the game starts, players will take turns shooting at each other's",True,WHITE)
                screen.blit(helptext, [10, 340])
                helptext = helpbodyfont.render("ships. A red circle signifies a hit while a white one a miss. The first",True,WHITE)
                screen.blit(helptext, [10, 355])
                helptext = helpbodyfont.render("player to sink all of their oppenents ships win!",True,WHITE)
                screen.blit(helptext, [10, 370])
                helptext = helpbodyfont.render("NOTE: This game currently doesn't contain the capability to say when a",True,WHITE)
                screen.blit(helptext, [10, 395])
                helptext = helpbodyfont.render("ship has been sunk. At this point, each side just needs to hit every dot",True,WHITE)
                screen.blit(helptext, [10, 410])

                pygame.draw.rect(screen,ORANGE,[190,450,120,35])
                helptext = helptitlefont.render("CONTINUE",True,WHITE)
                screen.blit(helptext, [195, 455])
                helptext = helpbodyfont.render("Click Here To",True,WHITE)
                screen.blit(helptext, [204, 435])

                pygame.display.flip()
                

        
        

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    
 
    # --- Drawing code should go here
    for i in range(len(gridX)):
        pygame.draw.rect(screen,gridcolor,[titlegridX[i],titlegridY[i],40,40], 3)
    for i in range(len(titlescreenshipsX)):
        pygame.draw.ellipse(screen, GREY, [titlescreenshipsX[i],titlescreenshipsY[i],35,35])
    pygame.draw.rect(screen,gridcolor,[430,70,68,400], 3)

    #displays the title
    startfont = pygame.font.SysFont('Calibri', 47, True, False)
    placetext = startfont.render("B  A  T  T  L  E  S  H  I  P",True,WHITE)
    screen.blit(placetext, [30, 20])
    
    #displays the computer option switch
    startfont = pygame.font.SysFont('Calibri', 13, True, False)
    comptext = startfont.render("Computer?",True,WHITE)
    screen.blit(comptext, [434, 74])
    startfont = pygame.font.SysFont('Calibri', 16, True, False)
    if computer == "off":
        pygame.draw.rect(screen,RED,[435,92,29,27])
        pygame.draw.rect(screen,GREY,[464,92,29,27])
        placetext = startfont.render("NO",True,WHITE)
        screen.blit(placetext, [438, 98])
    else:
        pygame.draw.rect(screen,GREEN,[464,92,29,27])
        pygame.draw.rect(screen,GREY,[435,92,29,27])
        placetext = startfont.render("YES",True,WHITE)
        screen.blit(placetext, [467, 98])    
    
    #displays the theme options
    startfont = pygame.font.SysFont('Calibri', 16, True, False)
    themetext = startfont.render("Themes",True,WHITE)
    screen.blit(themetext, [438, 125])

        #theme1
    pygame.draw.rect(screen,BLUE,[435,145,29,27])
    pygame.draw.rect(screen,DARKBLUE,[464,145,29,27])
    pygame.draw.rect(screen,theme1outline,[435,145,58,27], 2)

        #theme2
    pygame.draw.rect(screen,DARKBLUE,[435,175,29,27])
    pygame.draw.rect(screen,BLACK,[464,175,29,27])
    pygame.draw.rect(screen,theme2outline,[435,175,58,27], 2)

        #theme3
    pygame.draw.rect(screen,DARKBLUE,[435,205,29,27])
    pygame.draw.rect(screen,GREEN,[464,205,29,27])
    pygame.draw.rect(screen,theme3outline,[435,205,58,27], 2)

        #theme4
    pygame.draw.rect(screen,BLACK,[435,235,29,27])
    pygame.draw.rect(screen,DARKBLUE,[464,235,29,27])
    pygame.draw.rect(screen,theme4outline,[435,235,58,27], 2)

        #theme5
    pygame.draw.rect(screen,OCEAN,[435,265,29,27])
    pygame.draw.rect(screen,WAVE,[464,265,29,27])
    pygame.draw.rect(screen,theme5outline,[435,265,58,27], 2)

        #theme6
    pygame.draw.rect(screen,SEA,[435,295,29,27])
    pygame.draw.rect(screen,BISCOTI,[464,295,29,27])
    pygame.draw.rect(screen,theme6outline,[435,295,58,27], 2)

    #displays the game help option
    pygame.draw.rect(screen,ORANGE,[435,330,58,58])
    startfont = pygame.font.SysFont('Calibri', 25, True, False)
    helptext = startfont.render("HELP",True,WHITE)
    screen.blit(helptext, [437, 347])

    #displays the start game button
    pygame.draw.rect(screen,GREEN,[435,400,58,58])
    GOtext = startfont.render("GO!",True,WHITE)
    screen.blit(GOtext, [444, 417])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #killswitch
    if shipchoice>5:
        done = True

    # --- Limit to 60 frames per second
    clock.tick(60)

time.sleep(0.25)
if end != True:
    done = False
# -------- Setup Program Loop ----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            end = True

    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
                if (finalshipplacement == True) and (shipplacementX-(45*placershiplen)>-25):
                    orientation = "left"
                    directionchosen = True
            elif event.key == pygame.K_RIGHT:
                if (finalshipplacement == True) and (shipplacementX+(45*placershiplen)<490):
                    orientation = "right"
                    directionchosen = True
            elif event.key == pygame.K_UP:
                if (finalshipplacement == True) and (shipplacementY-(45*placershiplen)>-25):
                    orientation = "up"
                    directionchosen = True
            elif event.key == pygame.K_DOWN:
                if (finalshipplacement == True) and (shipplacementY+(45*placershiplen)<490):
                    orientation = "down"
                    directionchosen = True
            elif event.key == pygame.K_BACKSPACE:
                finalshipplacement = False
                orientation = "none"
                directionchosen = False
            elif (event.key == pygame.K_RSHIFT) or (event.key == pygame.K_LSHIFT):
                if selectposition == True and directionchosen == True:
                    if (shipchoice == 1) or (conflict == False):    
                        #tells the program to move to the next ship in the roster
                        shipchoice+=1
                        #the following code adds the ships individual points to a list depending on its directio
                        listchoiceX.append(shipplacementX)
                        listchoiceY.append(shipplacementY)
                        if orientation == "right":
                            finalshipplacementY = shipplacementY
                            for i in range(placershiplen-1):
                                finalshipplacementX = (shipplacementX+((i+1)*45))
                                listchoiceX.append(finalshipplacementX)
                                listchoiceY.append(finalshipplacementY)
                        if orientation == "left":
                            finalshipplacementY = shipplacementY
                            for i in range(placershiplen-1):
                                finalshipplacementX = (shipplacementX-((i+1)*45))
                                listchoiceX.append(finalshipplacementX)
                                listchoiceY.append(finalshipplacementY)
                        if orientation == "up":
                            finalshipplacementX = shipplacementX
                            for i in range(placershiplen-1):
                                finalshipplacementY = (shipplacementY-((i+1)*45))
                                listchoiceX.append(finalshipplacementX)
                                listchoiceY.append(finalshipplacementY)
                        if orientation == "down":
                            finalshipplacementX = shipplacementX
                            for i in range(placershiplen-1):
                                finalshipplacementY = (shipplacementY+((i+1)*45))
                                listchoiceX.append(finalshipplacementX)
                                listchoiceY.append(finalshipplacementY)
                        
                        selectposition = False
                    else:
                        #this makes the dots on the current ship flash red to inform the user that they can't place a ship in that position
                        PlacementColor = RED
                #the next two lines essentially reset the code for the next ship
                orientation = "none"
                finalshipplacement = False
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(backgroundcolor)

    #Mouse detection
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        
    # --- Game logic should go here

    #Set the conflicting ship position variable to False
    conflict = False

    """code that displays the current ship being placed"""
    if shipchoice == 1:
        placership = "Aircraft Carrier (5 spaces)"
        placershiplen = 5
    elif shipchoice == 2:
        placership = "Battleship (4 spaces)"
        placershiplen = 4
    elif shipchoice == 3:
        placership = "Destroyer (3 spaces)"
        placershiplen = 3
    elif shipchoice == 4:
        placership = "Submarine (3 spaces)"
        placershiplen = 3
    elif shipchoice == 5:
        placership = "Patrol Boat (2 spaces)"
        placershiplen = 2

    if placemode == True:
        startfont = pygame.font.SysFont('Calibri', 12, True, False)
        placetext = startfont.render("Please place your "+placership,True,WHITE)
        screen.blit(placetext, [25, 12])
        placetext = startfont.render("orientation: "+orientation,True,WHITE)
        screen.blit(placetext, [390, 12])

    if (finalshipplacement == False):
        directionchosen = False
        #code that follows the mouse
        for i in range(len(gridX)):
            if (mouseX-gridX[i]<45) and (mouseX-gridX[i]>0) and (mouseY-gridY[i]<45) and (mouseY-gridY[i]>0):
                pygame.draw.ellipse(screen, PlacementColor, [gridX[i]+2,gridY[i]+2,40,40])
                shipplacementX = gridX[i]+2
                shipplacementY = gridY[i]+2
        if pressed1:
            for i in range(len(listchoiceX)):
                if (listchoiceX[i] == shipplacementX) and (listchoiceY[i] == shipplacementY):
                    conflict = True
            if conflict == False:
                finalshipplacement = True
                selectposition = True

    #if the mouse is pressed on a point:
    if (finalshipplacement == True):
        if shipchoice == 1:
            conflict = False

        #the following code displays the current ship in the certain potential position and also gets those points in case the user selects that position
        pygame.draw.ellipse(screen, PlacementColor, [shipplacementX,shipplacementY,40,40])
        if orientation == "right":
            for i in range(placershiplen-1):
                drawshipplacementX = (shipplacementX+((i+1)*45))
                pygame.draw.ellipse(screen, PlacementColor, [drawshipplacementX,shipplacementY,40,40])
                for i in range(len(listchoiceX)):
                    if (listchoiceX[i] == drawshipplacementX) and (listchoiceY[i] == shipplacementY):
                        conflict = True
        if orientation == "left":
            for i in range(placershiplen-1):
                drawshipplacementX = (shipplacementX-((i+1)*45))
                pygame.draw.ellipse(screen, PlacementColor, [drawshipplacementX,shipplacementY,40,40])
                for i in range(len(listchoiceX)):
                    if (listchoiceX[i] == drawshipplacementX) and (listchoiceY[i] == shipplacementY):
                        conflict = True
        if orientation == "up":
            for i in range(placershiplen-1):
                drawshipplacementY = (shipplacementY-((i+1)*45))
                pygame.draw.ellipse(screen, PlacementColor, [shipplacementX,drawshipplacementY,40,40])
                for i in range(len(listchoiceX)):
                    if (listchoiceX[i] == shipplacementX) and (listchoiceY[i] == drawshipplacementY):
                        conflict = True
        if orientation == "down":
            for i in range(placershiplen-1):
                drawshipplacementY = (shipplacementY+((i+1)*45))
                pygame.draw.ellipse(screen, PlacementColor, [shipplacementX,drawshipplacementY,40,40])
                for i in range(len(listchoiceX)):
                    if (listchoiceX[i] == shipplacementX) and (listchoiceY[i] == drawshipplacementY):
                        conflict = True
            
    #resets the dot colors after they flash red:
    PlacementColor = GREY
        
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    
 
    # --- Drawing code should go here
    for i in range(len(gridX)):
        pygame.draw.rect(screen,gridcolor,[gridX[i],gridY[i],45,45], 3)
    for i in range(len(listchoiceX)):
        pygame.draw.ellipse(screen, GREY, [listchoiceX[i],listchoiceY[i],40,40])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #killswitch
    if shipchoice>5 and (turn == "player 2" or computer == "on"):
        done = True
        print ("1")
    elif shipchoice>5 and computer == "off":
        print("2")
        turn = "player 2"
        shipchoice = 1
        listchoiceX = compshipsX
        listchoiceY = compshipsY

    # --- Limit to 60 frames per second
    clock.tick(60)


# -------- Computer Setup Loop ---------
if end != True:
    done = False
if computer == "on":
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                end = True
            
        # --- Game logic should go here

        #Set the conflicting ship position variable to False
        conflict = False

        #set the ship being placed back to the first one
        shipchoice = 1

        #this while loop entirely dictates the position of the computer's ships
        while computerplacing == True:

            """code for tracking each ship"""
            if shipchoice == 1:
                placership = "Aircraft Carrier (5 spaces)"
                placershiplen = 5
            elif shipchoice == 2:
                placership = "Battleship (4 spaces)"
                placershiplen = 4
            elif shipchoice == 3:
                placership = "Destroyer (3 spaces)"
                placershiplen = 3
            elif shipchoice == 4:
                placership = "Submarine (3 spaces)"
                placershiplen = 3
            elif shipchoice == 5:
                placership = "Patrol Boat (2 spaces)"
                placershiplen = 2
            
            emptyspace = False
            restofcomputership = False

            #this while loop in particular finds a starting point for the current ship that isn't already taken. This loop does not however confirm that the rest of the ship can be placed in the surrounding area
            while emptyspace == False:
                emptyspace = True
                computershipstartpointX = (random.randint(0,9)*45)+27 #this plus 27 exists because of both the 25 pixel boundary and the 2 pixel spacing between the dots and their box
                computershipstartpointY = (random.randint(0,9)*45)+27 #the "rand.int(0,9)*45 is code that randomly chooses one of the 10 boxes in each axis
                if shipchoice != 1:
                    #this for loop sees of the box is already taken and potentially repeats the loop to find a new one
                    for i in range(len(compshipsX)):  
                        if (compshipsX[i] == computershipstartpointX) and (compshipsY[i] == computershipstartpointY):
                            emptyspace = False
            #this while loop is reponsible for placing the rest of each individual ship
            while restofcomputership == False:
                #this large if statement checks to see if the right direction is free of other ships
                if (computershipstartpointX+(placershiplen*45)<475):
                    if shipchoice != 1:
                        for i in range(placershiplen-1):
                            compshipplacementX = (computershipstartpointX+((i+1)*45))
                            for i in range(len(compshipsX)):
                                if (compshipsX[i] == compshipplacementX) and (compshipsY[i] == computershipstartpointY):
                                    directionfalse = True
                    if directionfalse == False:
                        directions.append("right")
                    directionfalse = False
                #this large if statement checks to see if the left direction is free of other ships
                if (computershipstartpointX-(placershiplen*45)>-25):
                    if shipchoice != 1:
                        for i in range(placershiplen-1):
                            compshipplacementX = (computershipstartpointX-((i+1)*45))
                            for i in range(len(compshipsX)):
                                if (compshipsX[i] == compshipplacementX) and (compshipsY[i] == computershipstartpointY):
                                    directionfalse = True
                    if directionfalse == False:
                        directions.append("left")
                    directionfalse = False
                #this large if statement checks to see if the up direction is free of other ships
                if (computershipstartpointY-(placershiplen*45)>-25):
                    if shipchoice != 1:
                        for i in range(placershiplen-1):
                            compshipplacementY = (computershipstartpointY-((i+1)*45))
                            for i in range(len(compshipsX)):
                                if (compshipsX[i] == computershipstartpointX) and (compshipsY[i] == compshipplacementY):
                                    directionfalse = True
                    if directionfalse == False:
                        directions.append("up")
                    directionfalse = False
                #this large if statement checks to see if the down direction is free of other ships
                if (computershipstartpointY+(placershiplen*45)<475):
                    if shipchoice != 1:
                        for i in range(placershiplen-1):
                            compshipplacementY = (computershipstartpointY+((i+1)*45))
                            for i in range(len(compshipsX)):
                                if (compshipsX[i] == computershipstartpointX) and (compshipsY[i] == compshipplacementY):
                                    directionfalse = True
                    if directionfalse == False:
                        directions.append("down")
                    directionfalse = False
                #if any of the directions are free, this code randomly chooses one of the available directions and places the ship along that direction. If there are no available directions, the whole while loop then repeats and finds another starting point
                if len(directions)>0:
                    choice = random.randint(1,len(directions))
                    placementchoice = directions[choice-1]
                    compshipsX.append(computershipstartpointX)
                    compshipsY.append(computershipstartpointY)
                    if placementchoice == "right":
                        finalcomputershipplacementY = computershipstartpointY
                        for i in range(placershiplen-1):
                            finalcomputershipplacementX = (computershipstartpointX+((i+1)*45))
                            compshipsX.append(finalcomputershipplacementX)
                            compshipsY.append(finalcomputershipplacementY)
                    if placementchoice == "left":
                        finalcomputershipplacementY = computershipstartpointY
                        for i in range(placershiplen-1):
                            finalcomputershipplacementX = (computershipstartpointX-((i+1)*45))
                            compshipsX.append(finalcomputershipplacementX)
                            compshipsY.append(finalcomputershipplacementY)
                    if placementchoice == "up":
                        finalcomputershipplacementX = computershipstartpointX
                        for i in range(placershiplen-1):
                            finalcomputershipplacementY = (computershipstartpointY-((i+1)*45))
                            compshipsX.append(finalcomputershipplacementX)
                            compshipsY.append(finalcomputershipplacementY)
                    if placementchoice == "down":
                        finalcomputershipplacementX = computershipstartpointX
                        for i in range(placershiplen-1):
                            finalcomputershipplacementY = (computershipstartpointY+((i+1)*45))
                            compshipsX.append(finalcomputershipplacementX)
                            compshipsY.append(finalcomputershipplacementY)

                    #the following print commands are useful to see how the computer finds and chooses coordinates
                    del directions[:]
                    print (directions)
                    print (placementchoice)
                    print (str(compshipsX)+"   "+str(compshipsY))
                    print (str(computershipstartpointX)+"   "+str(computershipstartpointY))

                    #these 3 lines reset the loop for the next ship
                    del directions[:]
                    restofcomputership = True
                    shipchoice+=1
                    
            #killswitch
            if shipchoice>5:
                computerplacing = False
                done = True
# -------- Main Program Loop -----------
turn = "player 1"
if end != True:
    done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            end = True
            
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(backgroundcolor)

    #seeing if a ship is sunk
    if (computer == "on"):
        sunkListStrings.clear()
        for i in range(len(compshipsX)):
            if (i<5):
                sunkID = 1
            elif (i<9):
                sunkID = 2
            elif (i<12):
                sunkID = 3
            elif (i<15):
                sunkID = 4
            elif (i<17):
                sunkID = 5
            for a in range(len(playershotsX)):
                if (playershotsX[a] == compshipsX[i]) and (playershotsY[a] == compshipsY[i]):
                    sunkList.append(sunkID)
        if (sunkList.count(1) != 5):
            sunkListStrings.append(" Aircraft Carrier")
        if (sunkList.count(2) != 4):
            sunkListStrings.append(" Battleship")
        if (sunkList.count(3) != 3):
            sunkListStrings.append(" Destroyer")
        if (sunkList.count(4) != 3):
            sunkListStrings.append(" Submarine")
        if (sunkList.count(5) != 2):
            sunkListStrings.append(" Patrol Boat")
    elif (computer == "off"):
        sunkListStrings.clear()
        if (turn == "player 1"):
            currentshipsX = compshipsX
            currentshipsY = compshipsY
            currentshotsX = playershotsX
            currentshotsY = playershotsY
        elif (turn == "player 2"):
            currentshipsX = playershipsX
            currentshipsY = playershipsY
            currentshotsX = compshotsX
            currentshotsY = compshotsY
            
        for i in range(len(currentshipsX)):
            if (i<5):
                sunkID = 1
            elif (i<9):
                sunkID = 2
            elif (i<12):
                sunkID = 3
            elif (i<15):
                sunkID = 4
            elif (i<17):
                sunkID = 5
            for a in range(len(currentshotsX)):
                if (currentshotsX[a] == currentshipsX[i]) and (currentshotsY[a] == currentshipsY[i]):
                    sunkList.append(sunkID)
        if (sunkList.count(1) != 5):
            sunkListStrings.append(" Aircraft Carrier")
        if (sunkList.count(2) != 4):
            sunkListStrings.append(" Battleship")
        if (sunkList.count(3) != 3):
            sunkListStrings.append(" Destroyer")
        if (sunkList.count(4) != 3):
            sunkListStrings.append(" Submarine")
        if (sunkList.count(5) != 2):
            sunkListStrings.append(" Patrol Boat")            

    startfont = pygame.font.SysFont('Calibri', 12, True, False)
    placetext = startfont.render("Ships left: "+str(sunkListStrings),True,WHITE)
    screen.blit(placetext, [20, 5])

    sunkList.clear()

    #the grid
    for i in range(len(gridX)):
        pygame.draw.rect(screen,gridcolor,[gridX[i],gridY[i],45,45], 3)
    
    # --- Game logic should go here
    enemylocation = False
    if turn == "player 1":
        # If you want a background image, replace this clear with blit'ing the
        # background image.

        hit = False
        fired = False

        pos = pygame.mouse.get_pos()
        mouseX = pos[0]
        mouseY = pos[1]
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        #code that follows the mouse
        for i in range(len(gridX)):
            if (mouseX-gridX[i]<45) and (mouseX-gridX[i]>0) and (mouseY-gridY[i]<45) and (mouseY-gridY[i]>0):
                pygame.draw.ellipse(screen, RED, [gridX[i]+2,gridY[i]+2,40,40])
                shotX = gridX[i]+2
                shotY = gridY[i]+2
        #placing a hit code
        if pressed1:
            fired = True
            alreadyshot = False
            for i in range(len(playershotsX)):
                if (shotX == playershotsX[i]) and (shotY == playershotsY[i]):
                    alreadyshot = True
                    fired = False
            if alreadyshot == False:
                playershotsX.append(shotX)
                playershotsY.append(shotY)
                for i in range(len(compshipsX)):
                    if (compshipsX[i] == shotX) and (compshipsY[i] == shotY):
                        playerhits+=1
                        hit = True
                        playershotcolor.append(RED)
                if hit == False:
                    playershotcolor.append(WHITE)

        for i in range(len(playershotsX)):
            pygame.draw.ellipse(screen, playershotcolor[i], [playershotsX[i],playershotsY[i],40,40])
        pygame.display.flip()
    if turn == "player 2":
        print ("shots taken: "+str(len(compshotsX)))
        if computer == "on":
            #a contingency in case the search_and_destroy protocol goes haywire
            if len(directions) == 0:
                search_and_destroy = False

            compalreadyshot = True
            hit = False
            fired = True
            if search_and_destroy == False:
                while compalreadyshot == True:
                    compalreadyshot = False
                    currentcompshotsX = (random.randint(0,9)*45)+27 #this plus 27 exists because of both the 25 pixel boundary and the 2 pixel spacing between the dots and their box
                    currentcompshotsY = (random.randint(0,9)*45)+27 #the "rand.int(0,9)*45 is code that randomly chooses one of the 10 boxes in each axis
                    for i in range(len(compshotsX)):  
                        if (compshotsX[i] == currentcompshotsX) and (compshotsY[i] == currentcompshotsY):
                            compalreadyshot = True
                compshotsX.append(currentcompshotsX)
                compshotsY.append(currentcompshotsY)
                for i in range(len(playershipsX)):
                    if (currentcompshotsX == playershipsX[i]) and (currentcompshotsY == playershipsY[i]):
                        comphits += 1
                        hit = True
                        compshotcolor.append(RED)

                        #setting up the search_and_destroy protocol
                        search_and_destroy = True
                        hitcompshotX = currentcompshotsX
                        hitcompshotY = currentcompshotsY

                        if (hitcompshotX-45>25):
                            directions.append("left")
                        if (hitcompshotX+45<475):
                            directions.append("right")
                        if (hitcompshotY-45>25):
                            directions.append("up")
                        if (hitcompshotY+45<475):
                            directions.append("down")
                if hit == False:
                    compshotcolor.append(WHITE)
            elif search_and_destroy == True:
                compalreadyshot = False
                hit = False

                print (directions)
                print (compshootdirection)
                
                if compshootdirection == "none":
                    hitcompshotX = currentcompshotsX
                    hitcompshotY = currentcompshotsY
                    choice = random.randint(1,len(directions))
                    print ("choice: "+str(choice-1))
                    compshootdirection = directions[choice-1]

                if compshootdirection == "up" and (hitcompshotY-45>25):
                    hitcompshotY-=45
                elif compshootdirection == "down" and (hitcompshotY+45<475):
                    hitcompshotY+=45
                elif compshootdirection == "left" and (hitcompshotX-45>25):
                    hitcompshotX-=45
                elif compshootdirection == "right" and (hitcompshotX+45<475):
                    hitcompshotX+=45
                else:
                    #if this else statement is ever activated, it means that the intended shot square is outside the grid, and the computer must recalibarate (therefore, fired = False because the computer cannot fire)
                    fired = False
                    directions.pop(choice-1)
                    compshootdirection = "none"
                print (compshootdirection)

                #this if statement exists in relation to the last comment
                if fired == True:
                    for i in range(len(compshotsX)):  
                        if (compshotsX[i] == hitcompshotX) and (compshotsY[i] == hitcompshotY):
                            compalreadyshot = True
                    if compalreadyshot == True:
                        print ("activated!")
                        hitcompshotX = currentcompshotsX
                        hitcompshotY = currentcompshotsY
                        directions.remove(compshootdirection)
                        compshootdirection = "none"
                        fired = False

                    if compalreadyshot == False:
                        compshotsX.append(hitcompshotX)
                        compshotsY.append(hitcompshotY)
                        for i in range(len(playershipsX)):
                            if (hitcompshotX == playershipsX[i]) and (hitcompshotY == playershipsY[i]):
                                hit = True
                        if hit == True:
                            compshotcolor.append(RED)
                            comphits += 1
                            #this code prevents the computer from shooting in any other directions once the directions of the ship is found
                            if compshootdirection == "up" or compshootdirection == "down":
                                try:
                                    directions.remove("left")
                                except Exception:
                                    nothing = 0
                                try:
                                    directions.remove("right")
                                except Exception:
                                    nothing = 0
                            if compshootdirection == "right" or compshootdirection == "left":
                                try:
                                    directions.remove("up")
                                except Exception:
                                    nothing = 0
                                try:
                                    directions.remove("down")
                                except Exception:
                                    nothing = 0
                        if hit == False:
                            compshotcolor.append(WHITE)
                            directions.remove(compshootdirection)
                            compshootdirection = "none"
                            hitcompshotX = currentcompshotsX
                            hitcompshotY = currentcompshotsY
           
                print (directions)
                print ("length of directions: "+str(len(directions)))
                print ("hitcompshotX: "+str(hitcompshotX))
                print ("hitcompshotY: "+str(hitcompshotY))
                print ("directions: "+str(compshootdirection))
                print ("hit? "+str(hit))
                print ("already shot? "+str(compalreadyshot))
                print (comphits)
                print (" ")
                    
        elif computer == "off":
            hit = False

            pos = pygame.mouse.get_pos()
            mouseX = pos[0]
            mouseY = pos[1]
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

            #code that follows the mouse
            for i in range(len(gridX)):
                if (mouseX-gridX[i]<45) and (mouseX-gridX[i]>0) and (mouseY-gridY[i]<45) and (mouseY-gridY[i]>0):
                    pygame.draw.ellipse(screen, RED, [gridX[i]+2,gridY[i]+2,40,40])
                    shotX = gridX[i]+2
                    shotY = gridY[i]+2
            #placing a hit code
            if pressed1:
                fired = True
                alreadyshot = False
                for i in range(len(compshotsX)):
                    if (shotX == compshotsX[i]) and (shotY == compshotsY[i]):
                        alreadyshot = True
                if alreadyshot == False:
                    compshotsX.append(shotX)
                    compshotsY.append(shotY)
                    for i in range(len(playershipsX)):
                        if (playershipsX[i] == shotX) and (playershipsY[i] == shotY):
                            comphits+=1
                            hit = True
                            compshotcolor.append(RED)
                    if hit == False:
                        compshotcolor.append(WHITE)

            for i in range(len(compshotsX)):
                pygame.draw.ellipse(screen, compshotcolor[i], [compshotsX[i],compshotsY[i],40,40])
        
        for i in range(len(compshotsX)):
            pygame.draw.ellipse(screen, compshotcolor[i], [compshotsX[i],compshotsY[i],40,40])
        pygame.display.flip()
            
        # --- Screen-clearing code goes here
 
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
 
    # --- Drawing code should go here
    

    #turn switch
    if turn == "player 2" and fired == True:
        time.sleep(0.25)
        turn = "player 1"
        fired = False
        for i in range(250):
            pygame.draw.rect(screen, BLACK, [250-i,250-i,(2*i),(2*i)])
            pygame.display.flip()
            time.sleep(0.0025)
    if turn == "player 1" and fired == True:
        time.sleep(0.25)
        turn = "player 2"
        fired = False
        for i in range(250):
            pygame.draw.rect(screen, BLACK, [250-i,250-i,(2*i),(2*i)])
            pygame.display.flip()
            time.sleep(0.0025)

    #winning/kill switch
    if playerhits >= 17:
        win = "player 1"
        done = True
        startfont = pygame.font.SysFont('Calibri', 24, True, False)
        placetext = startfont.render("Congrats Player 1",True,WHITE)
        screen.blit(placetext, [190, 240])
        pygame.display.flip()
        time.sleep(2)
    if comphits >= 17:
        win = "player 2"
        done = True
        startfont = pygame.font.SysFont('Calibri', 24, True, False)
        placetext = startfont.render("Congrats Player 2",True,WHITE)
        screen.blit(placetext, [190, 240])
        pygame.display.flip()
        time.sleep(2)

    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.

if end == False:
    os.execl(sys.executable, sys.executable, *sys.argv)
pygame.quit()
