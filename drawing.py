import pygame
from pygame.math import Vector2 as v2

def create_square(color: tuple, size: v2):
    surface = pygame.Surface(size)
    surface.fill(color)
    return surface

def create_circle(color: tuple, size: v2):
    surface = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
    pygame.draw.circle(surface, color, (size[0]//2, size[1]//2), size[0]//2)
    return surface

FONT_DICT = None

def draw_text(surface: pygame.Surface, pos: v2, text: str, size: int = 12, color: tuple = (255,255,255)):
    
    global FONT_DICT
    if FONT_DICT is None:
        pygame.font.init()
        FONT_DICT = {}
    if size not in FONT_DICT:
        FONT_DICT[size] = pygame.font.SysFont("monospace", size)

    text_surface = FONT_DICT[size].render(text, True, color)
    surface.blit(text_surface, pos)

