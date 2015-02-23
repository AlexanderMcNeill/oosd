import card

class Hand:
	cards = []

	def __init__(self):
		pass

	def displayHand(self):
		total = 0

		print("Your hand is:")
		for c in self.cards:
			c.display()
			total+= c.value

		print("Your total is: " + str(total))

	def displayCard(self, index):
		self.cards[cardIndex].display()

	def addCard(self, newCard):
		self.cards.append(newCard)

	def checkBust(self):
		total = 0

		for c in self.cards:
			total+= c.value

		if total > 21:
			return True
		else:
			return False