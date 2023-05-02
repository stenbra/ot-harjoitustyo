import pygame
from mechanics.scene import Scene
from mechanics.turn_handler import TurnHandler
from mechanics.player import Player

from ui.menu_button import MenuButton


class Game(Scene):
    def __init__(self, sceneName, players, cardpool, local_player_id, card_comparer, animation_handler):
        Scene.__init__(self, sceneName)
        button_font = pygame.font.Font('freesansbold.ttf', 24)
        main_menu_text = button_font.render("MENU", True, (0, 0, 0))
        lock_text = button_font.render("LOCK IN", True, (0, 0, 0))
        one_text = button_font.render("1", True, (0, 0, 0))
        two_text = button_font.render("2", True, (0, 0, 0))
        quit_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()
        
        self.quit_button = MenuButton(
            200, 50, quit_img, 6, 2, self.to_menu, main_menu_text)
        self.lock_in_button = MenuButton(
            1000, 600, quit_img, 8, 2, self.start, lock_text)
        self.marker_1 = MenuButton(
            0, 0, quit_img, 1, 1, None, one_text)
        self.marker_2 = MenuButton(
            0, 0, quit_img, 1, 1, None, two_text)

        self.marker_list = [self.marker_1, self.marker_2]

        card_hand_positions = [[400, 550], [500, 550], [
            600, 550], [700, 550], [800, 550], [900, 550]]

        self.players = players
        if len(self.players) == 1:
            self.players.append(Player("CO-Mput_ER"))
        self.card_comparer = card_comparer
        self.turn_handler = TurnHandler(
            self.players, cardpool, card_hand_positions, self.card_comparer, animation_handler)
        self.local_player_id = local_player_id

    def reset_scene(self):
        self.turn_handler.reset_turnhandler()

    def update(self):
        self.scenemanager.screen.fill((255, 255, 245))
        self.quit_button.update(self.scenemanager.screen)
        self.update_health()
        self.turn_handler.update()
        if self.turn_handler.state == 1:
            self.turn_handler.hands[self.local_player_id].update_cards(
                self.scenemanager.screen)
            self.lock_in_button.update(self.scenemanager.screen)
            marker_positions = self.turn_handler.hands[self.local_player_id].markers
            if len(marker_positions) > 0:
                for i in range(len(marker_positions)):
                    self.marker_list[i].set_pos(
                        marker_positions[i][0], marker_positions[i][1]-75)
                    self.marker_list[i].render(self.scenemanager.screen)

    def to_menu(self):
        self.scenemanager.set_active_scene("main-menu")

    def start(self):
        self.turn_handler.hands[self.local_player_id].play_selected()

    def update_health(self):
        for i in self.players:
            if i.id == self.local_player_id:
                i.health.health_bar.update_health_bar(
                    [30, 650], 300, 20, self.scenemanager.screen)
            else:
                i.health.health_bar.update_health_bar(
                    [950, 50], 300, 20, self.scenemanager.screen)
