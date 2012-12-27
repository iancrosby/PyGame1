import pygame
from pygame.locals import *
from custom_functions import *

pygame.init()

#Setting up some initialization stuff
done=False
size = [700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("PyGame1")
clock=pygame.time.Clock()

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

box_list = []
box1 = box(150, 50, (100, 50))
box_list.append(box1)

# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

    #Reset to basic state


    for event in pygame.event.get(): # User did something
        if event.type == QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for object in box_list:
                    if check_collision(event.pos, object):
                        print("click!")

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT



    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT



    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(white)

    font = pygame.font.Font(None, 25)
    text = font.render("My text",True,black)

    for object in box_list:
        pygame.draw.rect(screen,black,object.coordinates,2)
        c = object.coordinates
        screen.blit(text, [c[0]+10,c[1]+10])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    pygame.display.flip()





    # Limit to 20 frames per second
    clock.tick(20)