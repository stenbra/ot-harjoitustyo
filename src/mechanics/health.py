from ui.health_bar import HealthBar
class Health:
    def __init__(self,death_event, max_health=7):
        self.max_health = max_health
        self.current_health = max_health
        self.death_event = death_event
        self.health_bar = HealthBar(self)

    def take_damage(self, damage_amount):
        self.current_health = self.current_health-damage_amount
        if self.current_health <= 0:
            self.die()
    
    def die(self):
        self.death_event()
