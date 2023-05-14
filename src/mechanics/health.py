from ui.health_bar import HealthBar
from mechanics.call_back import call_back


class Health:
    def __init__(self, player , death_event, max_health=1):
        self.max_health = max_health
        self.current_health = max_health
        self.death_event = death_event
        self.health_bar = HealthBar(self)
        self.player = player

    def take_damage(self, damage_amount):
        if type(damage_amount) is tuple:
            damage= damage_amount[0]
        else:
            damage= damage_amount
        self.current_health = self.current_health-damage
        if self.current_health <= 0:
            self.die()

    def health_call_back(self,damage_amount):
        return call_back(self.take_damage,damage_amount)

    def die(self):
        self.death_event(self.player)
