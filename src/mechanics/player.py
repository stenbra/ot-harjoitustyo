import random


class Player:
    def __init__(self, name=""):
        self.health = None
        self.advantage = 0
        self.deck = ["GUARD", "ATTACK", "GUARDBREAK", "DODGE", "POKE"]
        self.id = random.random()*10000
        self.name = name

    def get_advantage(self):
        return self.advantage * 0.5

    def set_advantage(self, advantage):
        self.advantage = advantage
