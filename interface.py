import pygame
from pygame.math import Vector2 as v2
import world
import camera
import tilemap

class Interface:
    def __init__(self, w: world.World):
        self.world = w
        self.selected_entity = None
        self.camera = camera.Camera(32)

    def draw(self, surface: pygame.Surface):
        self.camera.set_surface(surface)

        self._draw_tilemap(self.world.tilemap)
        self._draw_entities(self.world.entities)
        
        if self.selected_entity is not None:
            pos = self.camera.map_to_screen(self.selected_entity.pos)
            pygame.draw.circle(surface, (255,255,0), pos, radius=self.camera.scale/2, width=2)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_click(v2(event.pos), event.button)

    def _handle_click(self, pos: v2, button: int):
        target = self.camera.screen_to_map(pos)

        if button == 1:
            self.selected_entity = self.world.get_entity_at(target)

    def _draw_entities(self, entities: list):
        for entity in entities:
            sprite = entity.get_sprite()
            if sprite is not None:
                self.camera.draw_sprite(sprite, entity.pos)

    def _draw_tilemap(self, tilemap: tilemap.Tilemap):

        viewed_tiles = self.camera.get_viewed_tiles()
        for x in range(viewed_tiles.left, viewed_tiles.right):
            for y in range(viewed_tiles.top, viewed_tiles.bottom):
                tile = tilemap.get_tile(v2(x, y))
                if tile is not None:
                    self.camera.draw_sprite(tile.sprite, v2(x, y))