import random
import card

class Deck(object):
	DECK_SIZE = 52
	HOUSE_SIZE = 13
	HOUSES = ["Spade","Club","Heart","Diamond"]
	cards = []

	def __init__(self):
		self.resetDeck()

	def resetDeck(self):
		currentHouse = 0
		cardCount = 0

		while cardCount < self.DECK_SIZE:
			house = self.HOUSES[currentHouse]
			value = (cardCount % self.HOUSE_SIZE) + 1

			self.cards.append(card.Card(house, value))

			cardCount+=1
			if(cardCount % self.HOUSE_SIZE == 0):
				currentHouse+=1

		random.shuffle(self.cards)

	def dealCard(self):
		return self.cards.pop()