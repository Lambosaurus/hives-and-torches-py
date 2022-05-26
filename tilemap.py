from pygame.math import Vector2 as v2
import pygame
import drawing

class Tile:
    def __init__(self, sprite: pygame.Surface):
        self.sprite = sprite
        self.passable = True
        
    def get_sprite(self):
        return self.sprite

class Tilemap:
    def __init__(self, tile_size: v2, size: tuple[int,int]):
        self._tiles = []
        self.size = size
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                row.append(None)
            self._tiles.append(row)

    def get_size(self) -> tuple[int,int]:
        return self.size

    def get_tile(self, pos: v2) -> Tile | None:
        return self._tiles[int(pos.y)][int(pos.x)]

    def set_tile(self, pos: v2, tile: Tile):
        self._tiles[int(pos.y)][int(pos.x)] = tile

TILE_DICT = None

def _load_tile_dict() -> dict[str:Tile]:
    return {
        "grass": Tile(drawing.create_square((20,100,20), v2(30,30))),
        "rock": Tile(drawing.create_square((80,80,80), v2(30,30))),
    }

def get_tile(name: str) -> Tile | None:
    global TILE_DICT
    if TILE_DICT == None:
        TILE_DICT = _load_tile_dict()
    return TILE_DICT[name]
