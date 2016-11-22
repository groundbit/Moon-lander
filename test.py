#Moon lander
# 1 - Import library
import pygame
from pygame.locals import *
import sys
import random

BLACKISH = [10, 10, 10]
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
# 2 - Initialize pygame
pygame.init()
width = 640
height = 480
MAX_WIDTH = width - 100
MAX_HEIGHT = height - 100

landerX = random.randrange(MAX_WIDTH)
landerY = random.randrange(MAX_HEIGHT)
landerRect = pygame.Rect(landerX, landerY, 100, 100)

screen= pygame.display.set_mode([width, height])

clock = pygame.time.Clock()
framesPerSecond = 30

#Gravity initalization
gravity = 1
xSpeed = 1
ySpeed = 1
# 3 - Load image(s)
lander = pygame.image.load("images/ball.gif")
lLeft = pygame.image.load("images/shiftR.png")
lRight = pygame.image.load("images/shiftL.png")
 
# 4 - Loop forever
while True:

    # 5 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()

    

        #Moving the lander
    keyPressedList = pygame.key.get_pressed()
     
    #--Moving Left       
    if keyPressedList[pygame.K_LEFT]:
        landerX = landerX - 3

    #--Moving Right
    if keyPressedList[pygame.K_RIGHT]:
        landerX = landerX + 3

    #--Moving Up
    if keyPressedList[pygame.K_UP]:
        landerY = landerY - 3

    #--Moving Down
    if keyPressedList[pygame.K_DOWN]:
        landerY = landerY + 0
        
        # See if user clicked
        if event.type == MOUSEBUTTONUP:
            mouseX, mouseY = event.pos
            
            # Check if the click was in the rect of the lander, if so, move lander to random new spot
            if landerRect.collidepoint( [mouseX, mouseY] ):
                landerX = random.randrange(MAX_WIDTH)
                landerY = random.randrange(MAX_HEIGHT)
                landerRect = pygame.Rect(landerX, landerY, 100, 100)
    
   # 6 - clear the screen before drawing it again
    screen.fill(BLACKISH)

    #Gravity simulation
    if (landerRect.left < 0) or (landerRect.right > WINDOW_WIDTH):
        xSpeed = -xSpeed

    if (landerRect.top < 0) or (landerRect.bottom > WINDOW_HEIGHT):
        ySpeed = gravity - ySpeed

    # update the rectangle of the ball, based on the speed in two directions
    #landerRect.left = landerRect.left + xSpeed
    landerRect.top = landerRect.top + ySpeed
    # 7 - draw the screen elements
    screen.blit(lander, (landerX, landerY))

    # 8 - update the screen
    pygame.display.update()

    # 9 slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount







