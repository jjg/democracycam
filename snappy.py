#!/usr/bin/python
# camera v4.02 (derived from example by Texy)
# for pi camera, and TFT set to 0 rotate
# takes picture,loads jpg and rotates onto TFT
#
from subprocess import call
import pygame, sys, os, time, datetime
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
time.sleep(0.5)
pygame.init()

DISPLAYSURF = pygame.display.set_mode((320, 240), 0, 32)

surf = pygame.Surface((240, 320)).convert()

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#pygame.mouse.set_visible(0)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

pygame.display.flip()
while True:

    start_time = time.time()
    filename = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d%H:%M:%S')+".jpg"
    argument="raspistill -o " + filename
    call ([argument], shell=True)
    print "argument = ",argument
    print "picture saved = ",filename
    print filename[-3:]
    time.sleep(0.25)
    if (filename[-3:] == "JPG") or (filename[-3:] == "jpg") :
        surf = pygame.image.load(filename)
        print "image load :",time.time() - start_time
        next_time = time.time()
        picture = pygame.transform.scale(surf, (320, 240))
        DISPLAYSURF.blit(picture,(0,0))
        print "rotate and scale :",time.time() - next_time

    pygame.display.flip()
    end_time = time.time()
    print "time taken :",end_time - start_time

# run the game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

