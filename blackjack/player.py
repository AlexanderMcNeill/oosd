import hand
import deck

class Player(object):

	def __init__(self, playerName):
		self.name = playerName
		self.isBust = False
		self.hand = hand.Hand()

	def hitMe(self, newCard):
		self.playerHand.addCard(newCard)
		self.bust = self.playerHand.checkBust()

	def setup(self, deck):
		hitMe(deck)
		hitMe(deck)

	def showHandStatus(self):
		self.hand.display()
		handTotal = self.hand.getTotal()
		print("The total is: " + str(handTotal))
