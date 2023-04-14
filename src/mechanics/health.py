class Health:
    def __init__(self,maxHealth=7):
        self.maxHealth = maxHealth
        self.currentHealth = maxHealth
    def TakeDamage(self,damageAmount):
        self.currentHealth = self.currentHealth-damageAmount
        if(self.currentHealth<=0):
            self.Die()
    def Die(self):
        pass