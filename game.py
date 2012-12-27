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

    #Reset to basic state
    draw_rect = False

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_rect = True

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT



    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT



    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(white)

    if draw_rect == True:
        pygame.draw.rect(screen,black,[20,20,250,100],2)

    font = pygame.font.Font(None, 25)

    text = font.render("My text",True,black)
    screen.blit(text, [250,250])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    pygame.display.flip()





    # Limit to 20 frames per second
    clock.tick(20)