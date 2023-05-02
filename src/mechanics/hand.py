from mechanics.deck import DrawPile
from ui.card import Card


class Hand:
    def __init__(self, player, cardpool, positions_list, turn_handler, hand_size=4):
        self.player = player
        self.draw_pile = DrawPile(player.deck)
        self.currentHand = {}
        self.cardpool = cardpool
        self.card_positions = positions_list
        self.draw_amount = hand_size
        self.turn_handler = turn_handler
        self.selected_cards = []
        self.locked = False
        self.markers = []

    def play_selected(self):
        self.locked = True
        card_list = []
        for i in range(len(self.selected_cards)):
            card = self.selected_cards.pop(0)
            for i in card:
                card_list.append(card[i])
        self.turn_handler.lock_in_cards(self.player, card_list)

    def set_selected(self, action, id):
        if self.locked == True:
            return
        for i in range(len(self.selected_cards)):
            if id in self.selected_cards[i]:
                self.currentHand[id].set_scale(1.2,1.2)
                deselected = self.selected_cards.pop(i)
                print("Deselected: " + deselected[id])
                self.update_marker_positions()
                return
        selected_card = {}
        selected_card[id] = action
        self.currentHand[id].set_scale(1.5, 1.5)
        self.selected_cards.append(selected_card)
        if len(self.selected_cards) > 2:
            deselected = self.selected_cards.pop(0)
            for i in deselected:
                self.currentHand[i].set_scale(1.2,1.2)
                print("Deselected: " + deselected[i])
        self.update_marker_positions()
        print("Selected: " + action)

    def update_marker_positions(self):
        self.markers = []
        for i in self.selected_cards:
            for id in i:
                self.markers.append(self.card_positions[int(id)])

    def new_hand(self):
        self.selected_cards = []
        self.currentHand = {}
        self.markers = []
        id = 0
        drawn_cards = self.draw_pile.draw(self.draw_amount)
        for i in drawn_cards:
            new_card = Card(self.set_selected, self.cardpool, i, id,self.player)
            new_card.set_pos(
                self.card_positions[id][0], self.card_positions[id][1])
            new_card.set_scale(1.2,1.2)
            self.currentHand[id] = new_card
            id += 1
        self.locked = False

    def update_cards(self, surface):
        for id in self.currentHand:
            self.currentHand[id].update(surface)
