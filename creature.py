

from turtle import position
from pygame.math import Vector2 as v2

class Creature:
    def __init__(self, pos: v2):
        self.pos = pos
        
    def get_sprite(self):
        return None
