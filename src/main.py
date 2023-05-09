import pygame
import mechanics.card_actions as actions
import mechanics.card_logic as logic
from mechanics.player import Player
from scenes.main_menu import MainMenuScene
from scenes.game import Game
from scenes.enter_name import EnterName
from mechanics.scenemanager import Scenemanager
from mechanics import animations
from mechanics.scoreboard import the_scoreboard


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('GUYINPINKSHORTS')
    clock = pygame.time.Clock()
    running = True

    reader = actions.ActionLoader()
    pool = logic.CardDataPool(reader)
    comparer = logic.CardComparer(reader)
    animation_handler = animations.AnimationHandler(screen)
    player = Player("player1")
    mainmenu = MainMenuScene("main-menu")
    name_scene = EnterName("name")
    game_scene = Game("game", [player], pool, player.id, comparer, animation_handler)
    scene_manager = Scenemanager([mainmenu, game_scene,name_scene], screen)
    scene_manager.set_active_scene("main-menu")
    print(the_scoreboard.scoreboard)
    for i in the_scoreboard.scoreboard.items():
        print("AHAA "+str(i))

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            events.append(event)

        screen.fill("purple")
        scene_manager.update(events)
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    clock.tick(60)


if __name__ == "__main__":
    main()
