import pygame
from pygame.math import Vector2 as v2
import world

class Interface:
    def __init__(self, w: world.World):
        self.world = w
        self.selected_entity = None

    def draw(self, surface: pygame.Surface):
        
        if self.selected_entity is not None:
            pos = self.world.camera.map_to_screen(self.selected_entity.pos)
            pygame.draw.circle(surface, (255,255,255), pos, 32)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click(v2(event.pos), event.button)

    def handle_click(self, pos: v2, button: int):
        target = self.world.camera.screen_to_map(pos)

        if button == 1:
            self.selected_entity = self.world.get_entity_at(target)