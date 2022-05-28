import pygame
from pygame.math import Vector2 as v2
import world
import camera
import tilemap
import creature
import drawing

class Interface:

    def __init__(self, w: world.World):
        self.world = w
        self.camera = camera.Camera(32)

        self._selected = None

    def draw(self, surface: pygame.Surface):
        self.camera.set_surface(surface)

        self._draw_tilemap(self.world.tilemap)
        self._draw_creatures(self.world.entities)

        if self._selected is not None:
            self._draw_selected(self._selected)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_click(v2(event.pos), event.button)

    def _handle_click(self, pos: v2, button: int):
        target = self.camera.screen_to_map(pos)

        if button == 1:
            self._selected = self.world.get_entity_at(target)

    def _draw_selected(self, entity: creature.Creature):
        pos = self.camera.map_to_screen(entity.pos)
        pygame.draw.circle(self.camera.surface, (255,255,0), pos, radius=self.camera.scale/2, width=2)
        self._draw_creature_stats(entity, v2(10, 10))

    def _draw_creature_stats(self, creature: creature.Creature, pos: v2, text_size: int = 16):
        # draw creature information
        text = f"{creature.name}"
        drawing.draw_text(self.camera.surface, pos, text, text_size)

        for i, key in enumerate(sorted(creature.stats.keys())):
            text = f"{key}: {creature[key]}"
            drawing.draw_text(self.camera.surface, pos + v2(0, (i+1)*text_size), text, text_size)

    def _draw_creatures(self, creatures: list[creature.Creature]):
        for creature in creatures:
            sprite = creature.get_sprite()
            if sprite is not None:
                self.camera.draw_sprite(sprite, creature.pos)

    def _draw_tilemap(self, tilemap: tilemap.Tilemap):
        viewed_tiles = self.camera.get_viewed_tiles()
        for x in range(viewed_tiles.left, viewed_tiles.right):
            for y in range(viewed_tiles.top, viewed_tiles.bottom):
                tile = tilemap.get_tile(v2(x, y))
                if tile is not None:
                    self.camera.draw_sprite(tile.sprite, v2(x, y))