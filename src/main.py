import pygame
import mechanics.card_actions as actions
import mechanics.card_logic as logic
from mechanics.player import Player
from main_menu import MainMenuScene
from game import Game
from mechanics.scenemanager import Scenemanager
from mechanics import animations


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    reader = actions.ActionLoader()
    pool = logic.CardDataPool(reader)
    comparer = logic.CardComparer(reader)
    animation_handler = animations.AnimationHandler(screen)
    player = Player("player1")
    mainmenu = MainMenuScene("main-menu")
    game_scene = Game("game", [player], pool, player.id, comparer, animation_handler)
    scene_manager = Scenemanager([mainmenu, game_scene], screen)
    scene_manager.set_active_scene("main-menu")

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        scene_manager.update()
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    clock.tick(60)


if __name__ == "__main__":
    main()
