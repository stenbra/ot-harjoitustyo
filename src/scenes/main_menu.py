import pygame
from ui.menu_button import MenuButton
from mechanics.scene import Scene
from mechanics.audio_resources import audio_resource

class MainMenuScene(Scene):
    def __init__(self, sceneName):
        Scene.__init__(self, sceneName)

        button_font = pygame.font.Font('freesansbold.ttf', 32)
        quit_text = button_font.render("QUIT", True, (0, 0, 0))
        continue_text = button_font.render("CONTINUE", True, (0, 0, 0))
        start_text = button_font.render("NEW GAME", True, (0, 0, 0))
        score_text = button_font.render("SCOREBOARD", True, (0, 0, 0))
        rules_text = button_font.render("GAME RULES", True, (0, 0, 0))
        quit_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()

        self.quit_button = MenuButton(
            640, 360, quit_img, 8, 2, self.end, quit_text)
        self.start_button = MenuButton(
            640, 280, quit_img, 8, 2, self.start, start_text)
        self.continue_button = MenuButton(
            640, 280, quit_img, 8, 2, self.continue_game, continue_text)
        self.score_button = MenuButton(
            640, 280, quit_img, 8, 2, self.to_score, score_text)
        self.rules_button = MenuButton(
            640, 280, quit_img, 8, 2, self.to_rules, rules_text)

        title_font = pygame.font.Font('freesansbold.ttf', 84)
        self.title = title_font.render(
            "THE PROVING GROUNDS", True, (0, 0, 0), (255, 255, 0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (640, 100)

    def update(self):
        self.scenemanager.screen.fill("red")
        self.scenemanager.screen.blit(self.title, self.title_rect)
        if self.scenemanager.get_scene_by_name("game").turn_handler.turn >0:
            self.continue_button.update(self.scenemanager.screen)
            self.start_button.set_pos(640,360)
            self.quit_button.set_pos(640,600)
            self.score_button.set_pos(640,440)
            self.rules_button.set_pos(640,520)
            self.start_button.update(self.scenemanager.screen)
            self.quit_button.update(self.scenemanager.screen)
            self.score_button.update(self.scenemanager.screen)
            self.rules_button.update(self.scenemanager.screen)
            return
        self.start_button.set_pos(640,280)
        self.quit_button.set_pos(640,520)
        self.score_button.set_pos(640,360)
        self.rules_button.set_pos(640,440)
        self.start_button.update(self.scenemanager.screen)
        self.quit_button.update(self.scenemanager.screen)
        self.score_button.update(self.scenemanager.screen)
        self.rules_button.update(self.scenemanager.screen)


    def end(self):
        """quits the application"""
        pygame.quit()
        quit()

    def continue_game(self):
        """changes the scene to game"""
        self.scenemanager.set_active_scene("game")

    def to_score(self):
        """changes the scene to score"""
        self.scenemanager.set_active_scene("score")
    
    def to_rules(self):
        """changes the scene to rules"""
        self.scenemanager.set_active_scene("rules")


    def start(self):
        """changes the scene to name and selects a random anouncer"""
        audio_resource.set_random_anouncer()
        self.scenemanager.set_active_scene("name")
        self.scenemanager.get_scene_by_name("name").reset_scene()

    def on_activate(self):
        pygame.mixer.music.unpause()
        return super().on_activate()