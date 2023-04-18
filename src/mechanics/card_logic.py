import pygame

class CardStats:
    def __init__(self,speed,damage,action):
        self.speed=speed
        self.action = action
        self.damage = damage
    def __str__(self):
        return "action "+str(self.action)+" speed "+str(self.speed)+" damage "+str(self.damage)

class CardComparer:
    def __init__(self,actionLoader):
        self.interactionDict = actionLoader.LoadActionInteractions()

    def compareCards(self,card1,card2,player1,player2):
        fasterCard = self.GetFasterCard(card1,card2,player1.get_advantage(),player2.get_advantage())
        if fasterCard == None:
            return False
        if fasterCard == 0:
            actionInfo= self.interactionDict[card1.action][card2.action]
            player1.set_advantage(actionInfo[0])
            player1.health.TakeDamage(actionInfo[1]*card2.damage)
            player2.set_advantage(actionInfo[2])
            player2.health.TakeDamage(actionInfo[3]*card1.damage)
        if fasterCard == 1:
            actionInfo= self.interactionDict[card2.action][card1.action]
            player2.set_advantage(actionInfo[0])
            player2.health.TakeDamage(actionInfo[1]*card2.damage)
            player1.set_advantage(actionInfo[2])
            player1.health.TakeDamage(actionInfo[3]*card1.damage)
        return True
        
    def GetFasterCard(self,card1,card2,p1a,p2a):
        if card1.speed+p1a>card2.speed+p2a:
            return 0
        if card1.speed+p1a<card2.speed+p2a:
            return 1
        if card1 in self.interactionDict["SAMETIMEPRIORITY"]:
            return 0
        if card2 in self.interactionDict["SAMETIMEPRIORITY"]:
            return 1
        return None
    
class CardPool:
    def __init__(self,actionLoader):
        self.cardStats = {}
        self.CreateCards(actionLoader.LoadActionBaseStats())
        self.cardVisuals = actionLoader.LoadActionVisuals()

    def CreateCards(self,cardData):
        for i in cardData:
            self.cardStats[i]= CardStats(float(cardData[i]["SPD"]),float(cardData[i]["DMG"]),str(i))

