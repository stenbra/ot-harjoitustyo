import random
import pygame



class CardStats:
    """simple class that holds three attributes
    
    Attributes:
        speed: the card speed
        action: the card action
        damage: the card damage
    """
    def __init__(self, speed, damage, action):
        self.speed = speed
        self.action = action
        self.damage = damage

    def __str__(self):
        return "action "+str(self.action)+" speed "+str(self.speed)+" damage "+str(self.damage)


class CardComparer:
    """ class that compares cards using data loaded from a card_interaction file

    Attributes:
        interaction_dict:The dictionar containing the interaction data

    """
    def __init__(self, action_loader):
        self.interaction_dict = action_loader.load_action_interactions()

    def compare_cards(self, card1, card2, player1, player2):
        """uses interaction_dict ad get_faster_card() to determine what the cards do (dmg/adv)

        Args:
            card1: a cardstats object containing data of the card that player 1 played
            card2: a cardstats object containing data of the card that player 2 played
            player1: player 1 used to get the advantage and to indext the dicionary
            player2: player 2 used to get the advantage and to indext the dicionary

        Returns: A dict of where the players are the keys and the values are the damage taken and advantage gain for the players
            there is also a key for which card was faster
        """
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
        """checks which card is played faster
        Args;
            card1: a cardstats object containing data of the card
            card2: a cardstats object containing data of the card
            p1a: the advantage of player1
            p2a: the advantage of player2
        Returns: 0 if card1 is faster,1 if card 2 is faster and None if they have the same speed
        """
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
    """class, that contains the data for all card "prefabs", 
    it also has a function that allows the computer to get random cards to play
    
    Attributes:
        card_stats: contains all the stats for the cards can be accessed by the card name
        card_visuals: contains title and image for the cards can be accessed by the card name
    """
    def __init__(self, action_loader):
        self.card_stats = {}
        self.create_cards(action_loader.load_action_base_stats())
        self.card_visuals = {}
        self.set_visual_recources(action_loader.load_action_visuals())

    def create_cards(self, card_data):
        """Generates the card stat dictionary based on the card data that it recieves

        Args:
            card_data: the data dictionary containing all the base stats for cards
        """
        for i in card_data:
            self.card_stats[i] = CardStats(
                float(card_data[i]["SPD"]), float(card_data[i]["DMG"]), str(i))

    def set_visual_recources(self, visual_data):
        """Generates the card visuals and puts them in a dictionary 

        Args:
            visual_data: the data dictionary containing the visual data for the cards
        """
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
        """gets random card actions from card_stats

        Args:
            action_amount: amount of actions to get
        Returns: a list of card actions
        """
        dict_keys = list(self.card_stats)
        actions = []
        for i in range(action_amount):
            action = random.randint(0, len(dict_keys)-2)
            actions.append(self.card_stats[dict_keys[action]].action)
        return actions
    