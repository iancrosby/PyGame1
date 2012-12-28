import pygame
from pygame.locals import *
from custom_functions import *

def local_star_loop(screen, star):

    red      = ( 255,   0,   0)
    white    = ( 255, 255, 255)
    done = False
    el = star.event_list


# -------- Main Program Loop -----------
    while done==False:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

        #Reset to basic state


        for event in pygame.event.get(): # User did something
            if event.type == QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for object in el:
                        if check_collision(event.pos, object):
                            print("click!")

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT



        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT



        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(white)

        for object in el:
            pygame.draw.ellipse(screen, red, object.coordinates, 0)
            c = object.coordinates
            screen.blit(object.text, [c[0]+40,c[1]-15])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        pygame.display.flip()
