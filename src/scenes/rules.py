import pygame
from ui.menu_button import MenuButton
from mechanics.scene import Scene
class RulesScene(Scene):
    def __init__(self, sceneName,cardpool):
        Scene.__init__(self, sceneName)
    
        button_font = pygame.font.Font('freesansbold.ttf', 32)
        self.text_font = pygame.font.Font('freesansbold.ttf', 40)
        to_menu_text = button_font.render("RETURN TO MENU", True, (0, 0, 0))
        general_text = button_font.render("HOW IT WORKS", True, (0, 0, 0))
        cards_text = button_font.render("CARDS", True, (0, 0, 0))
        interactions_text = button_font.render("INTERACTIONS", True, (0, 0, 0))
        quit_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()

        self.back_to_menu = MenuButton(
            640, 650, quit_img, 12, 2, self.to_menu, to_menu_text)
        self.general = MenuButton(
            300, 150, quit_img, 10, 2, self.set_general, general_text)
        self.interactions = MenuButton(
            640, 150, quit_img, 10, 2, self.set_interactions, interactions_text)
        self.cards = MenuButton(
            980, 150, quit_img, 10, 2, self.set_cards, cards_text)
        title_font = pygame.font.Font('freesansbold.ttf', 64)
        self.title = title_font.render(
            "GAME RULES", True, (0, 0, 0), (255, 150, 100))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (640, 75)
        self.view = 0
        self.cardpool = cardpool
   
    def render_turn_rules(self):
        pass
    def render_card_stats(self):
        pass
    def render_advantage_and_special_interactions(self):
        pass

    def update(self):
        self.scenemanager.screen.fill((200, 220, 255))
        self.scenemanager.screen.blit(self.title, self.title_rect)

        if self.view == 0:
            pass
        elif self.view==1:
            pass
        elif self.view==2:
            pass

        self.back_to_menu.update(self.scenemanager.screen)
        self.general.update(self.scenemanager.screen)
        self.interactions.update(self.scenemanager.screen)
        self.cards.update(self.scenemanager.screen)
    
    def set_general(self):
        self.view=0
    def set_cards(self):
        self.view=1
    def set_interactions(self):
        self.view=2
    def to_menu(self):
        self.scenemanager.set_active_scene("main-menu")

