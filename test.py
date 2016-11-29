# 1 - Import library
import pygame
from pygame.locals import *
import sys
import random
import math

BLACKISH = (10, 10, 10)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
#global var for objects
LANDER_MASS = 1
LANDER_FUEL = 100
PLANET_MASS = 7.347
PLANET_RADIUS = 1.079
GRAVITY = (9.8 * (PLANET_RADIUS ** 2))/ PLANET_MASS


def getVelocity (oAltitude, velocity):
    #landers alt = old alt + velocity + gravity
    nAltitude = oAltitude + velocity + 2
    return nAltitude
    
# 2 - Initialize pygame
pygame.init()
width = 648
height = 460
screen= pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
MAX_WIDTH = width - 100
MAX_HEIGHT = height - 100

landerX = 0
landerY = 0
xSpeed = 0
ySpeed = 0
landerRect = pygame.Rect(landerX, landerY, 50, 50)
#gravityCal =  (1 * 7.456)/(1079 + 1079)

# 3 - Load image(s)
lander = pygame.image.load("images/lander.gif")
landerRect =  lander.get_rect()


clock = pygame.time.Clock()  # set the speed (frames per second)

 
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
        xSpeed = xSpeed - .5
        

    #--Moving Right
    if keyPressedList[pygame.K_RIGHT]:
        xSpeed = xSpeed + .5
        

    #--Moving Up
    if keyPressedList[pygame.K_UP]:
        ySpeed = ySpeed - .5
        
        

    #--Moving Down
    if keyPressedList[pygame.K_DOWN]:
        ySpeed = ySpeed + .5
        
    landerX = landerX + xSpeed
    landerY = landerY + ySpeed
    landerY = getVelocity(landerY, ySpeed)

    
    
    # 6 - clear the screen before drawing it again
    screen.fill(BLACKISH)
    
    


    # update the rectangle of the lander, based on the speed in two directions
    #landerRect.left = landerRect.left + xSpeed + landerX
    #landerRect.top = landerRect.top + ySpeed - landerY

    landerRect = pygame.Rect(landerX, landerY, 50, 50)
    

    #  Could alternatively be written as:      landerRect = landerRect.move(xSpeed, ySpeed)

    #print landerRect
    screen.blit(lander, landerRect)
    

    # 8 - update the screen
    pygame.display.update()

    # 9 slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


