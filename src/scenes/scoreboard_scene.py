import pygame
from ui.menu_button import MenuButton
from mechanics.scene import Scene
from mechanics.scoreboard import the_scoreboard

class ScoreboardScene(Scene):
    def __init__(self, sceneName,show_amount=8,top_entry_pos=150):
        Scene.__init__(self, sceneName)
        
        self.score_entry_amount = show_amount

        button_font = pygame.font.Font('freesansbold.ttf', 32)
        self.score_font = pygame.font.Font('freesansbold.ttf', 40)
        to_menu_text = button_font.render("RETURN TO MENU", True, (0, 0, 0))
        continue_text = button_font.render("CONTINUE", True, (0, 0, 0))
        start_text = button_font.render("NEW GAME", True, (0, 0, 0))
        quit_img = pygame.image.load(
            "src/gamedata/sprites/button-base.png").convert_alpha()

        self.back_to_menu = MenuButton(
            640, 600, quit_img, 12, 2, self.to_menu, to_menu_text)
        title_font = pygame.font.Font('freesansbold.ttf', 64)
        self.title = title_font.render(
            "SCOREBOARD: TOP "+str(self.score_entry_amount), True, (0, 0, 0), (255, 220, 40))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (640, 100)
        self.top_entry_pos =top_entry_pos
        self.highlight = {}
    
    def render_scores(self):
        for i in the_scoreboard.scoreboard.items():
            if int(i[0]) > self.score_entry_amount:
                break
            name = str(i[1]["name"])
            index = str(i[0])+"."
            score = str(i[1]["score"])
            y_pos=self.top_entry_pos+40*int(i[0])
            if name in self.highlight:
                if str(self.highlight[name]) == score:
                    self.render_score_entry(index,300,y_pos,highlight=True)
                    self.render_score_entry(name,350,y_pos,highlight=True)
                    self.render_score_entry(score,980,y_pos,left_align=False,highlight=True)
                    continue
            self.render_score_entry(index,300,y_pos)
            self.render_score_entry(name,350,y_pos)
            self.render_score_entry(score,980,y_pos,False)

    def render_score_entry(self,text,x,y,left_align=True,highlight=False):
        if highlight:
            entry = self.score_font.render(
                    text, True,  (105, 0, 240))
        else:
            entry = self.score_font.render(
                    text, True,  (255, 220, 40))
        entry_rect = entry.get_rect()
        if left_align:
            entry_rect.topleft = (x, y)
        else:
            entry_rect.topright = (x, y)
        self.scenemanager.screen.blit(entry, entry_rect)

    def update(self):
        self.scenemanager.screen.fill("black")
        self.scenemanager.screen.blit(self.title, self.title_rect)
        self.back_to_menu.update(self.scenemanager.screen)
        self.render_scores()

    def to_menu(self):
        self.highlight = {}
        self.scenemanager.set_active_scene("main-menu")

