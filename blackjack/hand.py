import card

class Hand(object):
	
		
	def __init__(self):
		self.cards = []

	def displayHand(self):
		total = 0

		print("Hand is:")
		for c in self.cards:
			c.display()
			total+= c.value

		total = self.getTotal()
		print("Your total is: " + str(total))

	def displayCard(self, cardIndex):
		self.cards[cardIndex].display()

	def addCard(self, newCard):
		self.cards.append(newCard)

	def getTotal(self):
		total = 0

		for c in self.cards:
			total+= c.value

		return total

	def checkBust(self):
		total = 0

		for c in self.cards:
			total+= c.value

		if total > 21:
			return True
		else:
			return False