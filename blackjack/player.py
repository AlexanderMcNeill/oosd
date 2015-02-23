import hand
import deck

class Player:

	bust = False

	def __init__(self, playerName):
		self.playerHand = hand.Hand()
		self.playerName = playerName

	def hitMe(self, newCard):
		self.playerHand.addCard(newCard)
		self.playerHand.displayHand()
		self.bust = self.playerHand.checkBust()

	def playTurn(self, gameDeck):
		
		playing = True

		print(self.playerName + "'s turn")

		while playing == True and self.bust == False:
			
			self.hitMe(gameDeck.dealCard())

			if self.bust:
				print("You went bust!!")

			else:
				userOption = raw_input('Would you like another card (y, n)? ')

				while userOption not in ('y', 'n'):
					userOption = raw_input('Please enter vaild option. Would you like another card (y, n)? ')
				
				if userOption is 'y':
					playing = True
				else:
					playing = False
