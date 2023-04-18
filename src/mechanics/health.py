class Health:
    def __init__(self, max_health=7):
        self.maxHealth = max_health
        self.current_health = max_health

    def take_damage(self, damage_amount):
        self.current_health = self.current_health-damage_amount
        if self.current_health <= 0:
            self.die()

    def die(self):
        pass
