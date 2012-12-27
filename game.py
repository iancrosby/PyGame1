import pygame
pygame.init()

#Setting up some initialization stuff
done=False
size = [700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")
clock=pygame.time.Clock()

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)


# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(white)
    pygame.draw.rect(screen,black,[20,20,250,100],2)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(20)