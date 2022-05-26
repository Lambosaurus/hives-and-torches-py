import pygame
from pygame.math import Vector2 as v2
import camera
import tilemap
import map_gen
import creature


class World:
    def __init__(self):
        self.entities = []
        self.camera = camera.Camera()
        self.tilemap = tilemap.Tilemap(v2(32,32), (16,16))
        map_gen.generate_map(self.tilemap)

    def draw(self, surface: pygame.Surface):
        self.camera.set_surface(surface)

        self._draw_tilemap()
        
        for entity in self.entities:
            sprite = entity.get_sprite()
            if sprite is not None:
                self._draw_sprite(sprite, entity.pos)

    def add_entity(self, entity: creature.Creature):
        self.entities.append(entity)

    def get_entity_at(self, pos: v2) -> creature.Creature | None:
        for entity in self.entities:
            if entity.pos == pos:
                return entity
        return None
                
    def _draw_sprite(self, sprite: pygame.Surface, pos: v2):
        pos = self.camera.map_to_screen(pos)
        sprite_center = v2(sprite.get_size()) / 2
        self.camera.surface.blit(sprite, pos - sprite_center)

    def _draw_tilemap(self):
        size = self.tilemap.get_size()
        for x in range(size[0]):
            for y in range(size[1]):
                pos = v2(x,y)
                tile = self.tilemap.get_tile(pos)
                if tile is not None:
                    self._draw_sprite(tile.get_sprite(), pos)



