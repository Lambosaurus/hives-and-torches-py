import root
import creature
import world
import drawing
import interface
from pygame import Vector2 as v2


def main():
    game = root.Root()

    w = world.World()
    ui = interface.Interface(w)
    
    entity_sq = drawing.create_circle((200,50,50), v2(32,32))
    player = creature.Creature("John Goblikon", v2(0, 0), {
        "level": 3,
        "strength": 2,
        "intellect": -1,
        "speed": 30,
    })
    player.get_sprite = lambda: entity_sq
    w.add_entity(player)

    while game.run(ui.handle_event):

        ui.draw(game.window)
        game.end_frame()


if __name__ == "__main__":
    main()
