from mechanics.hand import Hand
from mechanics.health import Health
import time


class TurnHandler:
    def __init__(self, players, cardpool, card_positions, card_comparer, game_mode="PVE"):
        self.players = players
        self.cardpool = cardpool
        self.hands = {}
        self.card_positions = card_positions
        self.played_cards = []
        self.card_comparer = card_comparer
        self.state = 0
        self.setup_players()
        self.game_mode = game_mode

    def lock_in_cards(self, player, cards):
        player_cards = {}
        player_cards[player] = cards
        self.played_cards.append(player_cards)
        if self.game_mode == "PVE":
            self.set_computer_cards()
        if len(self.played_cards) >= 2:
            self.combat_phase()

    def set_computer_cards(self):
        computer_cards = {}
        computer_cards[self.players[1]
                       ] = self.cardpool.get_actions_for_computer_opponent()
        self.played_cards.append(computer_cards)

    def start_turn(self):
        self.state = 0
        for i in self.hands:
            self.hands[i].new_hand()
        self.state = 1

    def end_turn(self):
        self.state = 3
        self.played_cards = []
        time.sleep(0.5)
        self.start_turn()

    def combat_phase(self):
        self.state = 2
        players_cards = {}
        players = []
        for player_card_dict in self.played_cards:
            for player in player_card_dict:
                counter = 0
                cards_with_stats = []
                players.append(player)
                for card in player_card_dict[player]:
                    stats = self.cardpool.card_stats[card]
                    cards_with_stats.append(stats)
                    counter += 1
                # the 2 is a magic number which is the cardslot max, ill get back to this at some point hopefully
                for i in range(2-counter):
                    stats = self.cardpool.card_stats["NONE"]
                    cards_with_stats.append(stats)
                players_cards[player] = cards_with_stats
        for i in range(2):
            self.card_comparer.compare_cards(
                players_cards[players[0]][i], players_cards[players[1]][i], players[0], players[1])
            time.sleep(2)
        self.end_turn()

    def setup_players(self):
        for i in self.players:
            i.health = Health(self.player_death)
            player_hand = Hand(i, self.cardpool, self.card_positions, self)
            self.hands[i.id] = player_hand

    def player_death(self):
        pass
