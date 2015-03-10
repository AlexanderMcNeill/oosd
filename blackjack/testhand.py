import hand
import unittest
import card

class TestHandFunctions(unittest.TestCase):

	def setup(self):
		pass

	def test_addCard(self):
		newCard = card.Card("Spade", 7)

		self.hand = hand.Hand()
		self.hand.addCard(newCard)

		self.assertEqual(len(self.hand.cards), 1)

	def test_getTotal(self):
		newCard1 = card.Card("Spade", 7)
		newCard2 = card.Card("Spade", 6)

		self.hand = hand.Hand()
		self.hand.addCard(newCard1)
		self.hand.addCard(newCard2)

		handTotal = self.hand.getTotal()

		self.assertEqual(handTotal, 13)

	def test_displayCard(self):
		newCard = card.Card("Spade", 6)

		self.hand = hand.Hand()
		self.hand.addCard(newCard)

		response = self.hand.displayCard(0)
		
		self.assertEqual(response, "6 of Spade's")

	def test_display(self):
		newCard1 = card.Card("Spade", 7)
		newCard2 = card.Card("Hearts", 6)

		self.hand = hand.Hand()
		self.hand.addCard(newCard1)
		self.hand.addCard(newCard2)

		response = self.hand.display()
		self.assertEqual(response, "6 of Spade's")

if __name__ == '__main__':
    unittest.main()