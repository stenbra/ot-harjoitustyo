import random


class DrawPile:
    def __init__(self, card_list: list):
        self.card_pool = card_list
        self.deck_in_use = self.shuffle_new_deck()

    def draw(self, draw_amount):
        if draw_amount > len(self.card_pool):
            draw_amount = len(self.card_pool)
        if len(self.deck_in_use) < draw_amount:
            self.deck_in_use = self.shuffle_new_deck()
        hand = self.deck_in_use[0:draw_amount]
        self.deck_in_use = self.deck_in_use[draw_amount:]
        return hand

    def shuffle_new_deck(self):
        shuffled_deck = random.sample(self.card_pool, len(self.card_pool))
        return shuffled_deck
