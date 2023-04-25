import pygame


class Card:
    def __init__(self, scaleX, scaleY, onClick, cardPool, action, id):
        self.img = cardPool.card_visuals[action]["IMAGE"]
        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth*scaleX), int(self.imgHeight*scaleY)))
        self.rect = self.image.get_rect()
        self.action = action
        self.text = cardPool.card_visuals[action]["TITLE"]
        self.textRect = self.text.get_rect()
        self.onclick = onClick
        self.clicked = False
        self.id = id
        self.center_x = 0
        self.center_y = 0

    def click_check(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.onclick:
                    self.onclick(self.action, self.id)
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
        self.textRect.center = (x, y-100)
        self.rect.center = (x, y)
        self.center_x = x
        self.center_y = y

    def set_scale(self, x, y):
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth*x), int(self.imgHeight*y)))
        self.rect = self.image.get_rect()
        self.set_pos(self.center_x, self.center_y)
