import pygame
from pygame.locals import *
from custom_functions import *
from local_star import *

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

star_list = []
home_planet = star(50, 50, (100, 50))
mission = star(50, 50, (400, 300))
home_planet.label("Start world")
mission.label("Mission")

distress = d_event(30, 30, (200, 200))
distress.label("Distress signal")
mission.set_events([distress])

star_list.append(home_planet)
star_list.append(mission)


# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

    #Reset to basic state


    for event in pygame.event.get(): # User did something
        if event.type == QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for object in star_list:
                    if check_collision(event.pos, object):
                        if len(object.event_list) > 0:
                            local_star_loop(screen, object)
                        else:
                            print("click!")

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT



    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT



    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(white)

    for object in star_list:
        pygame.draw.ellipse(screen, green, object.coordinates, 0)
        c = object.coordinates
        screen.blit(object.text, [c[0]+40,c[1]-15])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    pygame.display.flip()


    # Limit to 20 frames per second
    clock.tick(20)