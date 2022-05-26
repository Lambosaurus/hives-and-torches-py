from pygame.math import Vector2 as v2
from pygame import Surface

class Camera:
    def __init__(self):
        self.pos = v2(0,0)
        self.tile_size = v2(32,32)
        self.surface = None
        self._set_screen_size(v2(0,0))

    def set_surface(self, surface: Surface):
        self._set_screen_size(v2(surface.get_size()))
        self.surface = surface

    def _set_screen_size(self, size: v2):
        self.size = size
        self.center = size / 2

    def map_to_screen(self, pos: v2):
        return ((pos - self.pos).elementwise() * self.tile_size) + self.center
