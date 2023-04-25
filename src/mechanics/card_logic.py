import pygame
import random


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
        print(card1.action,"vs",card2.action)
        print(str(player1.name)+" ADV: " + str(player1.get_advantage()))
        print(str(player2.name)+" ADV: " + str(player2.get_advantage()))
        if faster_card is None:
            return False
        if faster_card == 0:
            action_info = self.interaction_dict[card1.action][card2.action]
            player1.set_advantage(action_info[0])
            player1.health.take_damage(action_info[1]*float(card2.damage))
            player2.set_advantage(action_info[2])
            player2.health.take_damage(action_info[3]*float(card1.damage))

            print(card1.action+" was faster")
            print("Player: " + str(player1.name) + " increased advantage by "+ str(action_info[0]))
            print("Player: " + str(player1.name) + " took "+ str(action_info[1]) +" dmg")
            print("Player: " + str(player2.name) + " increased advantage by "+ str(action_info[2]))
            print("Player: " + str(player2.name) + " took "+ str(action_info[3]) +" dmg")

        if faster_card == 1:
            action_info = self.interaction_dict[card2.action][card1.action]
            player2.set_advantage(action_info[0])
            player2.health.take_damage(action_info[1]*float(card2.damage))
            player1.set_advantage(action_info[2])
            player1.health.take_damage(action_info[3]*float(card1.damage))

            print(card2.action+" was faster")
            print("Player: " + str(player2.name) + " increased advantage by "+ str(action_info[0]))
            print("Player: " + str(player2.name) + " took "+ str(action_info[1]) +" dmg")
            print("Player: " + str(player1.name) + " increased advantage by "+ str(action_info[2]))
            print("Player: " + str(player1.name) + " took "+ str(action_info[3]) +" dmg")
        return True

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
            
    def set_visual_recources(self,visual_data):
        for i in visual_data:
            visual_sub_dict={}
            card_text_font = pygame.font.Font('freesansbold.ttf', 14)
            text = card_text_font.render(
                str(visual_data[i]["TITLE"]), True, (0, 0, 0))
            visual_sub_dict["TITLE"] = text
            imagePath = "src/gamedata/sprites/" + \
                str(visual_data[i]["IMAGE"])
            img = pygame.image.load(imagePath).convert_alpha()
            visual_sub_dict["IMAGE"] = img
            self.card_visuals[i] = visual_sub_dict

    def get_actions_for_computer_opponent(self,action_amount=2):
        dict_keys = list(self.card_stats)
        actions =[]
        for i in range(action_amount):
            action = random.randint(0,len(dict_keys)-2)
            actions.append(self.card_stats[dict_keys[action]].action)
        return actions
        
