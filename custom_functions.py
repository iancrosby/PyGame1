import pygame
from pygame.locals import *

black    = (   0,   0,   0)

class star:
    '''A clickable star'''

    def __init__(self, x=1, y=1, p=(0,0)):

        self.update_coordinates(x, y, p)
        self.set_events([])

    def update_coordinates(self, x, y, p):

        #check that x, y, and p are the correct types
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(p, tuple)):
            raise TypeError

        #set new coordinates and collision points
        self.coordinates = [p[0], p[1], x, y]
        #collision points set as top left position and bottom right position
        self.collision = (p, (p[0]+x, p[1]+y))

    def label(self, text):
        '''Add a label to a box'''

        font = pygame.font.Font(None, 25)
        self.text = font.render(text,True,black)

    def set_events(self, event_list):
        '''Set the list of events within the star system. Each event is an event object.'''

        self.event_list = event_list




class d_event:
    '''A clickable dialogue event'''

    def __init__(self, x=1, y=1, p=(0,0)):

        self.update_coordinates(x, y, p)

    def update_coordinates(self, x, y, p):

        #check that x, y, and p are the correct types
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(p, tuple)):
            raise TypeError

        #set new coordinates and collision points
        self.coordinates = [p[0], p[1], x, y]
        #collision points set as top left position and bottom right position
        self.collision = (p, (p[0]+x, p[1]+y))

    def label(self, text):
        '''Add a label to a box'''

        font = pygame.font.Font(None, 25)
        self.text = font.render(text,True,black)

    def set_dialogue(self):
        '''Dialogue launched when event is clicked'''

        d1d = "Man are we glad to see you boys! This is ESS Monaco. We crossed paths with some asshole pirates that stripped our ship and left us to die. We're at your mercy. Whoever you are, please help us!"
        d2o = "Monaco this is the EDS Arkos. We stand ready to assist. Please advise what you need."
        d3o = "This is EDS Arkos. We are operating under Earth Emergency Directive 05 and require your immediate cooperation in the defense of Earth. Standby to receive further instructions."
        d4o = "Ignore their distress call."
        d5d = "Thank god! We've been stripped of everything other than a hull and some basic life support and food. We were on our way to the mining facility on Eos. If you could tow us there we could make our way from there."
        d6o = "We'll tow you home Monaco. Let's go."
        d7d = "THANK GOD!! YES!! We won't forget this Arkos!"
        d8o = "Sorry Monaco, that's too far out of our way. But here's some basic supplies. Good luck."
        d9d = "Well fuck. Okay, thanks for the supplies I guess. If you find anyone that could help, please send them our way."
        d10o = "Monaco, we can't go that far out of our way, but you're welcome to join our fleet for as long as it suits you."
        d11d = "I guess we don't have a lot of options at this point. We'll take you up on that but... ugh, I guess that's it then."
        d12d = "What... what are you talking about? We've got nothing but basic life support, what could we possible provide you? We're sitting ducks, please help us!"
        d13o = "Monaco, you are conscripted to the Earth Defence Force, Arkos Fleet. Prepare to receive a military command contingent that will relieve your Captain and reassign personnel."
        d14d = "You have GOT to be shitting me. All we have is worthless hunk of metal and a bunch of untrained civilians. I won't forget this. Monaco out."
        d15d = "Hello? Mayday! Mayday! Help us!! Where are you going??"

        dialogue = [d1d, [d2o, [d5d, [d6o, [d7d]],[d8o, [d9d]],[d10o, [d11d]]], [d3o, [d12d, [d13o, [d14d]]]], [d4o, [d15d]]]]
        self.dialogue = dialogue



def check_collision(p, co):
    '''Check if position p collides with object co'''

    if (p[0] >= co.collision[0][0]) and (p[0] <= co.collision[1][0]) and (p[1] >= co.collision[0][1]) and (p[1] <= co.collision[1][1]):
        return True

    return False



if __name__ == "__main__":
    #some light testing
    test_box = star(100, 100, (50,50))
    test_position_true = (60, 60)
    test_position_false = (151, 151)

    if not check_collision(test_position_true, test_box):
        raise AssertionError

    if check_collision(test_position_false, test_box):
        raise AssertionError









