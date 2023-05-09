import random
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
            card1, card2, player1.get_comp_advantage(), player2.get_comp_advantage())
        player_data = {}
        if faster_card is None:
            player_data[player1] = [card1.action,0,0]
            player_data[player2] = [card2.action,0,0]
            player_data["FASTER"] = None
        elif faster_card == 0:
            action_info = self.interaction_dict[card1.action][card2.action]
                
            player_data[player1] = [card1.action,action_info[0],action_info[1]*float(card2.damage)]
            player_data[player2] = [card2.action,action_info[2],action_info[3]*float(card1.damage)]
            player_data["FASTER"] = player1

        elif faster_card == 1:
            action_info = self.interaction_dict[card2.action][card1.action]        
            player_data[player1] = [card1.action,action_info[2],action_info[3]*float(card2.damage)]
            player_data[player2] = [card2.action,action_info[0],action_info[1]*float(card1.damage)]
            player_data["FASTER"] = player2
        return player_data

    def get_faster_card(self, card1, card2, p1a, p2a):
        if card1.speed-p1a < card2.speed-p2a:
            return 0
        if card1.speed-p1a > card2.speed-p2a:
            return 1
        if card1 in self.interaction_dict["SAMETIMEPRIORITY"]:
            return 0
        if card2 in self.interaction_dict["SAMETIMEPRIORITY"]:
            return 1
        return None


class CardDataPool:
    def __init__(self, action_loader):
        self.card_stats = {}
        self.create_cards(action_loader.load_action_base_stats())
        self.card_visuals = {}
        self.set_visual_recources(action_loader.load_action_visuals())

    def create_cards(self, card_data):
        for i in card_data:
            self.card_stats[i] = CardStats(
                float(card_data[i]["SPD"]), float(card_data[i]["DMG"]), str(i))

    def set_visual_recources(self, visual_data):
        for i in visual_data:
            visual_sub_dict = {}
            card_text_font = pygame.font.Font('freesansbold.ttf', 14)
            text = card_text_font.render(
                str(visual_data[i]["TITLE"]), True, (0, 0, 0))
            visual_sub_dict["TITLE"] = text
            image_path = "src/gamedata/sprites/" + \
                str(visual_data[i]["IMAGE"])
            img = pygame.image.load(image_path).convert_alpha()
            visual_sub_dict["IMAGE"] = img
            self.card_visuals[i] = visual_sub_dict

    def get_actions_for_computer_opponent(self, action_amount=2):
        dict_keys = list(self.card_stats)
        actions = []
        for i in range(action_amount):
            action = random.randint(0, len(dict_keys)-2)
            actions.append(self.card_stats[dict_keys[action]].action)
        return actions
    