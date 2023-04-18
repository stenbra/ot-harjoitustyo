import pygame
from ui.menu_button import MenuButton
from ui.scene import Scene

class MainMenuScene(Scene):
    def __init__(self,sceneName):
        Scene.__init__(self,sceneName)

        buttonFont = pygame.font.Font('freesansbold.ttf', 32)
        quitText= buttonFont.render("QUIT",True,(0,0,0))
        startText= buttonFont.render("START",True,(0,0,0))
        quit_img = pygame.image.load("src/gamedata/sprites/button-base.png").convert_alpha()
        
        self.quitButton = MenuButton(640,360,quit_img,8,2,self.end,quitText)
        self.startButton = MenuButton(640,280,quit_img,8,2,self.start,startText)
        
        titleFont = pygame.font.Font('freesansbold.ttf', 56)
        self.title = titleFont.render("LE GAME",True,(0,0,0),(255,255,0))
        self.titleRect= self.title.get_rect()
        self.titleRect.center = (640,100)

    def update(self):
        self.scenemanager.screen.fill("red")
        self.startButton.update(self.scenemanager.screen)
        self.quitButton.update(self.scenemanager.screen)
        self.scenemanager.screen.blit(self.title, self.titleRect)

    def end(self):
        pygame.quit()
        quit()
        
    def start(self):
        self.scenemanager.set_active_scene("game")