import player
import deck
import hand

class House(player.Player):
	HOUSE_NAME = "house"


	def __init__(self):
		playerHand = hand.Hand()
		self.playerName = playerName

	def setup(gameDeck):
		self.hitMe(gameDeck.dealCard())
		
		self.hitMe(gameDeck.dealCard())

		print("The House shows their first card and leaves the other card face down")
		self.playerHand.displayCard(0)