from game.casting.actor import Actor
from game.shared.point import Point
import random

class Gem (Actor):

    def __init__(self):
        super().__init__()
    
    def fall(self,max_y):
        x = self._position.get_x()
        y = (self._position.get_y()+5) % max_y
        self._position = Point(x,y)

    def changingX(self):
        x = random.randint(1,59)*15
        self._position = Point(x,self._position.get_y())
