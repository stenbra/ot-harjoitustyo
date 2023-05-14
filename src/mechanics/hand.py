from mechanics.deck import DrawPile
from ui.card import Card


class Hand:
    """A class, which handles the selection and order of cards to be played and submitted in a turn
        also sets up and updates the cards that will be rendered
    Attributes:
        player: the player owning the hand
        draw_pile: A draw pile from which cards will be drawn
        currentHand: a dictionary of the cards in the hand
        cardpool: object with all card data
        card_positions: positions for where to instantiate and render cards
        draw_amount: amount of cards to draw
        turn_handler: reference to the turnhandler object that instatiated this class
        selected_cards:list of cards that are currently selected
        locked: bool for wether the cards are locked in or not
        markers: a list of postions of the selected cards so that the marker can be set at the right place
    """
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
        """Commits the selected cards to the turn handler in the order they where selected"""
        self.locked = True
        card_list = []
        for i in range(len(self.selected_cards)):
            card = self.selected_cards.pop(0)
            for i in card:
                card_list.append(card[i])
        self.turn_handler.lock_in_cards(self.player, card_list)

    def set_selected(self, action, id):
        """Updates(selects/deselects) the selected_cards list based on the id of the card that was clicked
            also updates the marker positions

        Args:
            action: action of the card, this is passed on to the turnhandler when locking in cards
            id: the cards own id, select and deselect cards
        """
        if self.locked == True:
            return
        for i in range(len(self.selected_cards)):
            if id in self.selected_cards[i]:
                self.currentHand[id].set_scale(1.2,1.2)
                deselected = self.selected_cards.pop(i)
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
        self.update_marker_positions()

    def update_marker_positions(self):
        """updates the list of marker positons based on seleced cards
        """
        self.markers = []
        for i in self.selected_cards:
            for id in i:
                self.markers.append(self.card_positions[int(id)])

    def new_hand(self):
        """Gnereates/draws a new hand with new cards that it initializes and sets the position of
        """
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
        """Updates the ui and click check of the cards in hand"""
        for id in self.currentHand:
            self.currentHand[id].update(surface)
