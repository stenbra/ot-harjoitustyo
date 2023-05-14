import random
from mechanics.call_back import call_back

class Player:
    """class, containing info and stats about the player

    Attributes:
        health: the health object attached to the player
        is_bot: true if the player is the computer otherwise false
        advantage: the advantage the player has used in UI
        deck: the deck the player has
        id: an id attached to the player
        advantage_multiplier: decides how effective the advantage is
        comparison_advantage: the advantage the player has used when generateing combat data
    """
    def __init__(self, name="", is_bot = False):
        self.health = None
        self.is_bot =is_bot
        self.advantage = 0 #only for visuals
        self.deck = ["GUARD", "ATTACK", "GUARDBREAK", "DODGE", "POKE","GUARD", "ATTACK", "GUARDBREAK", "DODGE", "POKE"]
        self.id = random.random()*10000
        self.name = name
        self.advantage_multiplier = 0.5
        self.comparison_advantage =0 #used in card comparisons
        
    def get_advantage(self):
        """gets the player advantage, used in ui
        
        Returns: player advantage
        """
        return self.advantage * self.advantage_multiplier
    
    def get_comp_advantage(self):
        """gets the player advantage, used in data generation
        
        Returns: player advantage
        """
        return self.comparison_advantage * self.advantage_multiplier

    def set_advantage(self, advantage):
        """sets the visual advantage and comparison_advantage
        Args:
            advantage: the advantage amount to be set
        """
        if type(advantage) is tuple:
            adv= advantage[0]
        else:
            adv= advantage
        self.advantage = adv
        self.set_comparison_advantage(adv)

    def set_comparison_advantage(self, advantage):
        """only sets the comparison_advantage
        
        Args:
            advantage: the advantage amount to be set
        """
        self.comparison_advantage = advantage

    def set_advantage_callback(self,advantage):
        """wraps set_avantage in a callback
        Args:
            advantage: the advantage amount to be set
        Returns: the callback
        """
        return call_back(self.set_advantage,advantage)
