import player
import deck
import hand

class House(player.Player):
	HOUSE_NAME = "house"


	def __init__(self):
		super(House, self).__init__("House")

	def setup(self, gameDeck):
		self.hitMe(gameDeck.dealCard())
		
		self.hitMe(gameDeck.dealCard())

		print("The House shows their first card and leaves the other card face down")
		self.playerHand.displayCard(0)

	def playTurn(self, gameDeck):
		
		playing = True

		print("//////////////////////////////////////////////////////////////////////")
		print("It is the " + self.name + "'s turn")
		
		print(self.name + "'s current hand is:")
		self.showHandStatus()

		while playing == True and self.bust == False:

			newCard = gameDeck.dealCard()

			print(self.name + " is dealt the " + newCard.display())
			
			self.hitMe(newCard)
			self.showHandStatus()

			if self.playerHand.getTotal() > 16:
				print(self.name + " house stands")
				playing = False
			if self.bust:
				print(self.playerName  + " went bust!!")
