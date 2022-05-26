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

def draw_text(surface: pygame.Surface, text: str, color: tuple = (255,255,255), size: int = 8, font: str = "Arial", pos: v2 = (0,0)):
    font = pygame.font.SysFont(font, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

