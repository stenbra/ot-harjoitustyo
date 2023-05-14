from ui.health_bar import HealthBar
from mechanics.call_back import call_back


class Health:
    """class which handles health points for players
    
    Attributes:
        max_health: the maximum amount of hitpoints
        current_health the current amount of hitpoints
        death_event: function to be called on death
        health_bar: The ui of the health
        player: the player "owning" the health
    """
    def __init__(self, player , death_event, max_health=7):
        self.max_health = max_health
        self.current_health = max_health
        self.death_event = death_event
        self.health_bar = HealthBar(self)
        self.player = player

    def take_damage(self, damage_amount):
        """ updates the healthbar based on the damage amount, calls die if health is zero or below

        Args:
            damage_amount: the amount of health to be lost, can be a tuple if this was called from the callback
        """
        if type(damage_amount) is tuple:
            damage= damage_amount[0]
        else:
            damage= damage_amount
        self.current_health = self.current_health-damage
        if self.current_health <= 0:
            self.die()

    def health_call_back(self,damage_amount):
        """wraps take damage into a callback
        Args:
            damage_amount: the amount of health to be lost
        Returns: a callback funtion
        """
        return call_back(self.take_damage,damage_amount)

    def die(self):
        """calls the death_event"""
        self.death_event(self.player)
