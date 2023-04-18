import pygame
import mechanics.card_actions as actions
import mechanics.card_logic as logic
from main_menu import MainMenuScene
from mechanics.scenemanager import Scenemanager


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    reader = actions.ActionLoader()
    pool = logic.CardPool(reader)
    print(str(pool.card_stats['GUARD']))
    mainmenu = MainMenuScene("main-menu")
    sceneManager = Scenemanager([mainmenu], screen)
    sceneManager.set_active_scene("main-menu")

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        sceneManager.update()
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

    clock.tick(60)


if __name__ == "__main__":
    main()
