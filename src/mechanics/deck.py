import random


class DrawPile:
    """class that functions like a deck for any list of objects
    Attributes:
        card_pool: the list of objects that can be drawn
        deck_in_use: a shuffled list of objects that can be reduced based on card_pool 
    """
    def __init__(self, card_list: list):
        self.card_pool = card_list
        self.deck_in_use = self.shuffle_new_deck()

    def draw(self, draw_amount):
        """returns x amount of objects from deck_in_use
            shuffle the deck if the draw exeeds the current amount in the deck
            maxdraw amount is the size of the card_pool
        Args:
            draw_amount: amount of things to draw
        Returns: a list of drawn things
        """
        if draw_amount > len(self.card_pool):
            draw_amount = len(self.card_pool)
        if len(self.deck_in_use) < draw_amount:
            self.deck_in_use = self.shuffle_new_deck()
        hand = self.deck_in_use[0:draw_amount]
        self.deck_in_use = self.deck_in_use[draw_amount:]
        return hand

    def shuffle_new_deck(self):
        """shuffles a list
        
        Returns: a shuffled version of the card_pool
        """
        shuffled_deck = random.sample(self.card_pool, len(self.card_pool))
        return shuffled_deck
