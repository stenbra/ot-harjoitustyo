import pygame


class MenuButton:
    def __init__(self, x, y, image, scaleX, scaleY, onClick, text):
        imgWidth = image.get_width()
        imgHeight = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(imgWidth*scaleX), int(imgHeight*scaleY)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = text
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.onclick = onClick
        self.clicked = False

    def click_check(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.onclick:
                    self.onclick()
                    self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

    def render(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text, (self.textRect.x, self.textRect.y))

    def update(self, surface):
        self.render(surface)
        self.click_check()
    
    def set_pos(self, x, y):
        self.textRect.center = (x, y)
        self.rect.center = (x, y)
