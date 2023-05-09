import random
from mechanics.call_back import call_back

class Player:
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
        return self.advantage * self.advantage_multiplier
    
    def get_comp_advantage(self):
        return self.comparison_advantage * self.advantage_multiplier

    def set_advantage(self, advantage):
        if type(advantage) is tuple:
            adv= advantage[0]
        else:
            adv= advantage
        self.advantage = adv
        self.set_comparison_advantage(adv)

    def set_comparison_advantage(self, advantage):
        self.comparison_advantage = advantage

    def set_advantage_callback(self,advantage):
        return call_back(self.set_advantage,advantage)
