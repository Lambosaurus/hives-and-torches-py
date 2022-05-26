import root
import creature
import world
import drawing
from pygame import Vector2 as v2


def main():
    game = root.Root()

    w = world.World()
    
    entity_sq = drawing.create_circle((200,50,50), v2(32,32))

    unit = creature.Creature(v2(0, 0))
    unit.get_sprite = lambda: entity_sq
    w.entities.append(unit)
    
    while game.run():

        w.draw(game.window)

        game.end_frame()


if __name__ == "__main__":
    main()
