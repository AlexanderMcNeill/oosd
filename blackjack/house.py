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

		print(self.playerName + "'s turn")
		
		self.playerHand.displayHand()

		while playing == True and self.bust == False:
			self.hitMe(gameDeck.dealCard())
			self.playerHand.displayHand()

			if self.playerHand.getTotal() > 16:
				playing = False
			if self.bust:
				print(self.playerName  + " went bust!!")
