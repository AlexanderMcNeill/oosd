import hand
import deck

class Player(object):

	def __init__(self, playerName):
		self.playerName = playerName
		self.isBust = False
		self.playerHand = hand.Hand()

	def hitMe(self, newCard):
		self.playerHand.addCard(newCard)
		self.bust = self.playerHand.checkBust()

	def setup(self, deck):
		hitMe(deck)
		hitMe(deck)

	def playTurn(self, gameDeck):
		
		playing = True

		print(self.playerName + "'s turn")


		while playing == True and self.bust == False:
			self.hitMe(gameDeck.dealCard())
			self.playerHand.displayHand()

			if self.bust:
				print("House bust!!")

			else:
				userOption = raw_input('Would you like another card (y, n)? ')

				while userOption not in ('y', 'n'):
					userOption = raw_input('Please enter vaild option. Would you like another card (y, n)? ')
				
				if userOption is 'y':
					playing = True
				else:
					playing = False
