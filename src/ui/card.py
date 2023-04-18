import pygame


class card:
    def __init__(self, scaleX, scaleY, onClick, cardPool, action):

        cardFont = pygame.font.Font('freesansbold.ttf', 32)
        text = cardFont.render(
            str(cardPool.card_visuals[action]["TITLE"]), True, (0, 0, 0))
        imagePath = "src/gamedata/sprites/" + \
            str(cardPool.card_visuals[action]["IMAGE"])
        self.img = pygame.image.load(imagePath).convert_alpha()
        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth*scaleX), int(self.imgHeight*scaleY)))
        self.rect = self.image.get_rect()
        self.action = action
        self.text = text
        self.textRect = self.text.get_rect()
        self.onclick = onClick
        self.clicked = False

    def click_check(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.onclick:
                    self.onclick(self.action)
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

    def set_scale(self, x, y):
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth*x), int(self.imgHeight*y)))