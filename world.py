from pygame.math import Vector2 as v2
import tilemap
import map_gen
import creature


class World:
    def __init__(self):
        scale = 32
        self.entities = []
        self.tilemap = tilemap.Tilemap((16,16))
        map_gen.generate_map(self.tilemap)

    def add_entity(self, entity: creature.Creature):
        self.entities.append(entity)

    def get_entity_at(self, pos: v2) -> creature.Creature | None:
        for entity in self.entities:
            if entity.pos == pos:
                return entity
        return None


