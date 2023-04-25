import pygame

class HealthBar:
    def __init__(self,health):
        self.health = health
        self.back_ground_color = (205,205,205)
        self.bar_color = (255,95,95)

    def update_health_bar(self,postion,width,height,surface):
        health_percentage = self.health.current_health/self.health.max_health
        pygame.draw.rect(surface,self.back_ground_color,(postion[0],postion[1],width,height))
        pygame.draw.rect(surface,self.bar_color,(postion[0],postion[1],width*health_percentage,height))