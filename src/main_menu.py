import pygame
from ui.menu_button import MenuButton
from mechanics.scene import Scene


class MainMenuScene(Scene):
    def __init__(self, sceneName):
        Scene.__init__(self, sceneName)

        button_font = pygame.font.Font('freesansbold.ttf', 32)
        quit_text = button_font.render("QUIT", True, (0, 0, 0))
        start_text = button_font.render("START", True, (0, 0, 0))
        quit_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()

        self.quit_button = MenuButton(
            640, 360, quit_img, 8, 2, self.end, quit_text)
        self.start_button = MenuButton(
            640, 280, quit_img, 8, 2, self.start, start_text)

        title_font = pygame.font.Font('freesansbold.ttf', 84)
        self.title = title_font.render(
            "VERY EPIC GAME-TITLE", True, (0, 0, 0), (255, 255, 0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (640, 100)

    def update(self):
        self.scenemanager.screen.fill("red")
        self.start_button.update(self.scenemanager.screen)
        self.quit_button.update(self.scenemanager.screen)
        self.scenemanager.screen.blit(self.title, self.title_rect)

    def end(self):
        pygame.quit()
        quit()

    def start(self):
        self.scenemanager.set_active_scene("game")
