import unittest
from mechanics.deck import DrawPile


class DeckFunctionalityTests(unittest.TestCase):
    def setUp(self):
        cardslist = ["PA", "B", "A", "A", "B", "QA"]
        self.deck = DrawPile(cardslist)

    def test_construction(self):
        cardslist = ["PA", "B", "A"]
        deck = DrawPile(cardslist)
        self.assertAlmostEqual(deck.card_pool, cardslist)
        self.assertEqual(len(deck.deck_in_use), len(cardslist))

    def test_draw_returns_right_amount(self):
        hand = self.deck.draw(3)
        self.assertEqual(len(hand), 3)

    def test_draw_right_amout_remaining_in_deck(self):
        hand = self.deck.draw(3)
        self.assertEqual(len(self.deck.deck_in_use), len(self.deck.card_pool)-3)

    def test_reshuffle_deck_when_enough_cards_left(self):
        hand = self.deck.draw(3)
        deckPreShuffle = self.deck.deck_in_use
        hand1 = self.deck.draw(5)
        deckPostShuffle = self.deck.deck_in_use
        self.assertNotEqual(deckPreShuffle, deckPostShuffle)
        self.assertEqual(len(hand1), 5)

    def test_draw_only_entire_deck_when_giving_too_large_draw(self):
        hand = self.deck.draw(90)
        self.assertEqual(len(hand), len(self.deck.card_pool))
