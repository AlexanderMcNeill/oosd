import hand
import deck

class Player(object):

	def __init__(self, playerName):
		self.name = playerName
		self.isBust = False
		self.hand = hand.Hand()

	def hitMe(self, newCard):
		self.hand.addCard(newCard)

		if self.hand.getTotal() > 21:

			self.isBust = True

	def setup(self, deck):
		self.hitMe(deck.dealCard())
		self.hitMe(deck.dealCard())

	def showHandStatus(self):
		self.hand.display()
		handTotal = self.hand.getTotal()
		print("The total is: " + str(handTotal))
