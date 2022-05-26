import tilemap
import random
from pygame.math import Vector2 as v2

def generate_map(t: tilemap.Tilemap):

    grass = tilemap.get_tile("grass")
    rock = tilemap.get_tile("rock")

    size = t.get_size()
    for x in range(size[0]):
        for y in range(size[1]):
            t.set_tile(v2(x,y), grass)
    for _ in range(16):
        pos = v2(random.randint(0, size[0]-1), random.randint(0, size[1]-1))
        t.set_tile(pos, rock)
