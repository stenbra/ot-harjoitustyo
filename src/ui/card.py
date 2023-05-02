import pygame


class Card:
    def __init__(self, onClick, cardPool, action, id, player):
        card_text_font = pygame.font.Font('freesansbold.ttf', 14)
        cardstats = cardPool.card_stats[action]
        spd_text = card_text_font.render("SPD: "+str(cardstats.speed -player.get_advantage()), True, (0, 0, 0))
        dmg_text = card_text_font.render("DMG: "+str(cardstats.damage), True, (0, 0, 0))


        self.img = cardPool.card_visuals[action]["IMAGE"]
        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth), int(self.imgHeight)))
        self.rect = self.image.get_rect()
        self.action = action
        self.title_text = cardPool.card_visuals[action]["TITLE"]
        self.title_rect = self.title_text.get_rect()
        self.spd_text = spd_text
        self.spd_rect = self.spd_text.get_rect()
        self.dmg_text = dmg_text
        self.dmg_rect = self.dmg_text.get_rect()
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
        surface.blit(self.title_text, (self.title_rect.x, self.title_rect.y))
        surface.blit(self.spd_text, (self.spd_rect.x, self.spd_rect.y))
        surface.blit(self.dmg_text, (self.dmg_rect.x, self.dmg_rect.y))

    def update(self, surface):
        self.render(surface)
        self.click_check()

    def set_pos(self, x, y):
        self.title_rect.center = (x, y+105)
        self.spd_rect.center = (x, y+120)
        self.dmg_rect.center= (x,y+135)
        self.rect.center = (x, y)
        self.center_x = x
        self.center_y = y

    def set_scale(self, x, y):
        self.image = pygame.transform.scale(
            self.img, (int(self.imgWidth*x), int(self.imgHeight*y)))
        self.rect = self.image.get_rect()
        self.set_pos(self.center_x, self.center_y)
