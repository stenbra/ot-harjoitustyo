import pygame


class CardStats:
    def __init__(self, speed, damage, action):
        self.speed = speed
        self.action = action
        self.damage = damage

    def __str__(self):
        return "action "+str(self.action)+" speed "+str(self.speed)+" damage "+str(self.damage)


class CardComparer:
    def __init__(self, action_loader):
        self.interaction_dict = action_loader.load_action_interactions()

    def compare_cards(self, card1, card2, player1, player2):
        faster_card = self.get_faster_card(
            card1, card2, player1.get_advantage(), player2.get_advantage())
        if faster_card is None:
            return False
        if faster_card == 0:
            action_info = self.interaction_dict[card1.action][card2.action]
            player1.set_advantage(action_info[0])
            player1.health.take_damage(action_info[1]*card2.damage)
            player2.set_advantage(action_info[2])
            player2.health.take_damage(action_info[3]*card1.damage)
        if faster_card == 1:
            action_info = self.interaction_dict[card2.action][card1.action]
            player2.set_advantage(action_info[0])
            player2.health.TakeDamage(action_info[1]*card2.damage)
            player1.set_advantage(action_info[2])
            player1.health.take_damage(action_info[3]*card1.damage)
        return True

    def get_faster_card(self, card1, card2, p1a, p2a):
        if card1.speed+p1a > card2.speed+p2a:
            return 0
        if card1.speed+p1a < card2.speed+p2a:
            return 1
        if card1 in self.interaction_dict["SAMETIMEPRIORITY"]:
            return 0
        if card2 in self.interaction_dict["SAMETIMEPRIORITY"]:
            return 1
        return None


class CardPool:
    def __init__(self, action_loader):
        self.card_stats = {}
        self.create_cards(action_loader.load_action_base_stats())
        self.card_visuals = action_loader.load_action_visuals()

    def create_cards(self, card_data):
        for i in card_data:
            self.card_stats[i] = CardStats(
                float(card_data[i]["SPD"]), float(card_data[i]["DMG"]), str(i))
