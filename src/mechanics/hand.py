from mechanics.deck import DrawPile


class Hand:
    def __init__(self, player):
        self.player = player
        self.draw_pile = DrawPile(player.deck)