import pygame
import mechanics.card_actions as actions
import mechanics.card_logic as logic
from mechanics.player import Player
from scenes.main_menu import MainMenuScene
from scenes.game import Game
from scenes.enter_name import EnterName
from scenes.scoreboard_scene import ScoreboardScene
from scenes.rules import RulesScene
from mechanics.scenemanager import Scenemanager
from mechanics import animations
from mechanics.scoreboard import the_scoreboard
from ui.animations.character_anim_rescource import anim_resource 

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('GUYINPINKSHORTS')
    clock = pygame.time.Clock()
    running = True

    anim_resource.Initialize()
    reader = actions.ActionLoader()
    pool = logic.CardDataPool(reader)
    comparer = logic.CardComparer(reader)
    animation_handler = animations.AnimationHandler(screen)
    player = Player("player1")
    mainmenu = MainMenuScene("main-menu")
    name_scene = EnterName("name")
    game_scene = Game("game", [player], pool, player.id, comparer, animation_handler)
    score_scene = ScoreboardScene("score")
    rules_scene = RulesScene("rules",pool)
    scene_manager = Scenemanager([mainmenu, game_scene,name_scene,score_scene,rules_scene], screen)
    scene_manager.set_active_scene("main-menu")
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
