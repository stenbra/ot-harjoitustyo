class Player:
    def __init__(self, health):
        self.health = health
        self.advantage = 0
        self.deck = ["GUARD", "ATTACK", "GUARDBREAK", "DODGE", "BLOCK"]

    def get_advantage(self):
        return self.advantage * 0.5

    def set_advantage(self, advantage):
        self.advantage = advantage
