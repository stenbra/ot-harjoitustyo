import pygame
from ui.menu_button import MenuButton
from mechanics.scene import Scene
from mechanics.audio_resources import audio_resource


class EnterName(Scene):
    def __init__(self, sceneName,max_length=24):
        Scene.__init__(self, sceneName)
        title_font = pygame.font.Font('freesansbold.ttf', 64)
        self.title = title_font.render(
            "ENTER NAME", True, (0, 0, 0), (255, 0, 0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (640, 100)

        button_font = pygame.font.Font('freesansbold.ttf', 32)
        start_text = button_font.render("START", True, (0, 0, 0))
        main_menu_text = button_font.render("BACK TO MENU", True, (0, 0, 0))
        button_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()
        self.start_button = MenuButton(
            640, 440, button_img, 8, 2, self.start, start_text)
        self.quit_button = MenuButton(
            200, 50, button_img, 10, 2, self.to_menu, main_menu_text)
        
        self.challenger_name=""
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(self.challenger_name, True, (0, 0, 0))
        self.rect = pygame.Rect(390, 180, 500, 40)
        self.max_char_count = max_length
        self.max_char_amount = button_font.render(
            "NAME CAN'T BE LONGER THAN "+str( self.max_char_count)+" CHARACTERS", True, (0, 0, 0), (200, 0, 0))
        self.max_char_amount_rect = self.max_char_amount.get_rect()
        self.max_char_amount_rect.center = (640, 300)

        self.name_empty = button_font.render(
            "NAME CAN'T BE EMPTY", True, (0, 0, 0), (200, 0, 0))
        self.name_empty_rect = self.name_empty.get_rect()
        self.name_empty_rect.center = (640, 300)
        self.name_empty_check = False

    def text_handling(self):
         for event in self.scenemanager.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.challenger_name = self.challenger_name[:-1]
                elif len(self.challenger_name) >=self.max_char_count:
                    return
                else:
                    self.challenger_name += event.unicode
                self.txt_surface = self.font.render(self.challenger_name, True, (0, 0, 0))
            
    def update(self):
        self.text_handling()
        self.scenemanager.screen.fill((245,225,60))
        self.scenemanager.screen.blit(self.title, self.title_rect)
        if self.challenger_name =="" and self.name_empty_check == True:
            self.scenemanager.screen.blit(self.name_empty, self.name_empty_rect)
        if len(self.challenger_name) >=self.max_char_count:
            self.scenemanager.screen.blit(self.max_char_amount, self.max_char_amount_rect)
        pygame.draw.rect(self.scenemanager.screen,(20,20,20),(395, 185, 505, 45))
        pygame.draw.rect(self.scenemanager.screen,(255,255,255),self.rect)
        self.scenemanager.screen.blit(self.txt_surface, (self.rect.x, self.rect.y))
        self.start_button.update(self.scenemanager.screen)
        self.quit_button.update(self.scenemanager.screen)
        
    def start(self):
        if self.challenger_name =="":
            self.name_empty_check = True
            return
        self.scenemanager.set_active_scene("game")
        self.scenemanager.get_scene_by_name("game").reset_scene()
        self.scenemanager.get_scene_by_name("game").set_player_name_in_pve(self.challenger_name)

    def reset_scene(self):
        self.name_empty_check = False
        self.challenger_name=""
        self.txt_surface = self.font.render(self.challenger_name, True, (0, 0, 0))
    
    def to_menu(self):
        self.scenemanager.set_active_scene("main-menu")

    def on_activate(self):
        audio_resource.play_anouncer_sound("NAME")
        pygame.mixer.music.pause()
        return super().on_activate()