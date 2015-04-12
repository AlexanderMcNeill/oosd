import card

class Hand(object):
	
		
	def __init__(self):
		self.cards = []

	def display(self):
		for c in self.cards:
			c.display()

	def displayCard(self, cardIndex):
		self.cards[cardIndex].display()

	def addCard(self, newCard):
		self.cards.append(newCard)

	def getTotal(self):
		total = 0

		for c in self.cards:
			total+= c.value

		return total