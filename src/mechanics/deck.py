import random
class Deck:
    def __init__(self,cardList):
        self.cardPool = cardList
        self.deckInUse = self.shuffleNewDeck()

    def draw(self,drawAmount):
        if drawAmount>len(self.cardPool):
            drawAmount =len(self.cardPool)
        if len(self.deckInUse) < drawAmount:
            self.deckInUse = self.shuffleNewDeck()
        hand = self.deckInUse[0:drawAmount]
        self.deckInUse = self.deckInUse[drawAmount:]
        return hand

    def shuffleNewDeck(self):
        shuffledDeck= random.shuffle(self.cardPool)
        return shuffledDeck