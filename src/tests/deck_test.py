import unittest
from mechanics.deck import DrawPile

class DeckFunctionalityTests(unittest.TestCase):
    def setUp(self):
        cardslist = ["PA","B","A","A","B","QA"]
        self.deck = DrawPile(cardslist)

    def test_construction(self):
        cardslist = ["PA","B","A"]
        deck = DrawPile(cardslist)
        self.assertAlmostEqual(deck.cardPool,cardslist)
        self.assertEqual(len(deck.deckInUse),len(cardslist))
    
    def test_draw_returns_right_amount(self):
        hand = self.deck.draw(3)
        self.assertEqual(len(hand),3)
    
    def test_draw_right_amout_remaining_in_deck(self):
        hand = self.deck.draw(3)
        self.assertEqual(len(self.deck.deckInUse),len(self.deck.cardPool)-3)

    def test_reshuffle_deck_when_enough_cards_left(self):
        hand = self.deck.draw(3)
        deckPreShuffle = self.deck.deckInUse
        hand1= self.deck.draw(5)
        deckPostShuffle = self.deck.deckInUse
        self.assertNotEqual(deckPreShuffle,deckPostShuffle)
        self.assertEqual(len(hand1),5)

    def test_draw_only_entire_deck_when_giving_too_large_draw(self):
        hand= self.deck.draw(90)
        self.assertEqual(len(hand),len(self.deck.cardPool))