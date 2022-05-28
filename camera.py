from pygame.math import Vector2 as v2
import pygame
import math
import util

class Camera:
    def __init__(self, scale: int = 32):
        self.pos = v2(0,0) # position of the camera in tiles
        self.scale = scale # pixels per tile
        self.surface = None
        self._set_screen_size(v2(0,0))

    def set_surface(self, surface: pygame.Surface):
        self._set_screen_size(v2(surface.get_size()))
        self.surface = surface

    def _set_screen_size(self, size: v2):
        self.size = size
        self.center = size / 2 # in pixels

    def map_to_screen(self, pos: v2):
        # returns screen pixels given tile coordinates
        return ((pos - self.pos) * self.scale) + self.center

    def screen_to_map(self, pos: v2):
        # returns tile coordinates given screen pixels
        return util.v2_mutate((pos - self.center) / self.scale + self.pos, round)

    def get_viewed_tiles(self) -> pygame.Rect:
        # returns the tiles that are currently visible
        tile_half_span = util.v2_mutate(self.center / self.scale, math.ceil)
        return pygame.Rect(self.pos - tile_half_span, tile_half_span * 2)

    def draw_sprite(self, sprite: pygame.Surface, pos: v2):
        # draws a sprite at the given tile coordinates
        sprite_center = v2(sprite.get_size()) / 2
        self.surface.blit(sprite, self.map_to_screen(pos) - sprite_center)

