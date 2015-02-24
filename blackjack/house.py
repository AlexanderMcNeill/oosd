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
		self.hand.displayCard(0)

	def playTurn(self, gameDeck):

		print("//////////////////////////////////////////////////////////////////////")
		print("It is the " + self.name + "'s turn")
		
		print(self.name + "'s current hand is:")
		self.showHandStatus()

		if self.hand.getTotal() > 16 and not self.isBust:
			print(self.name + " house stands")
			playing = False
		elif self.isBust:
			print(self.name  + " went bust!!")

		while self.isBust == False and self.hand.getTotal() < 16:

			newCard = gameDeck.dealCard()

			print(self.name + " is dealt the ")
			newCard.display()
			
			self.hitMe(newCard)

			print(self.name + "'s current hand is:")
			self.showHandStatus()

			if self.hand.getTotal() > 16 and not self.isBust:
				print(self.name + " house stands")
				playing = False
			elif self.isBust:
				print(self.name  + " went bust!!")
