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

    player = creature.Creature(v2(0, 0))
    player.get_sprite = lambda: entity_sq
    w.add_entity(player)
    
    while game.run(ui.handle_event):

        ui.draw(game.window)
        game.end_frame()


if __name__ == "__main__":
    main()
