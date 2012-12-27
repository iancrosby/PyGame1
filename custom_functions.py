import pygame
from pygame.locals import *

class box:
    '''A clickable box'''

    def __init__(self, x=1, y=1, p=(0,0)):

        self.update_coordinates(x, y, p)
        self.set_visible(True)

    def update_coordinates(self, x, y, p):

        #check that x, y, and p are the correct types
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(p, tuple)):
            raise TypeError

        #set new coordinates and collision points
        self.coordinates = [p[0], p[1], x, y]
        #collision points set as top left position and bottom right position
        self.collision = (p, (p[0]+x, p[1]+y))

    def set_visible(self, vis):
        '''set whether the box is visible or not'''

        if not isinstance(vis, bool):
            raise TypeError

        else:
            self.visible = vis

def check_collision(p, co):
    '''Check if position p collides with object co'''

    if (p[0] >= co.collision[0][0]) and (p[0] <= co.collision[1][0]) and (p[1] >= co.collision[0][1]) and (p[1] <= co.collision[1][1]):
        return True

    return False

if __name__ == "__main__":
    #some light testing
    test_box = box(100, 100, (50,50))
    test_position_true = (60, 60)
    test_position_false = (151, 151)

    if not check_collision(test_position_true, test_box):
        raise AssertionError

    if check_collision(test_position_false, test_box):
        raise AssertionError









