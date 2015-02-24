import deck
import player
import house

class BlackJack(object):
	VALID_INPUTS = {'y', 'Y', 'n', 'N'}
	def __init__(self):
		self.deck = deck.Deck()
		self.players = []
		

	#Method that sets up all the game players
	def setupPlayers(self):
		numPlayers = raw_input("How many players (max players 5)? ")

		#Keeping on asking for valid input untill vaild input is put in

		converted = False

		while converted == False:
			try:
				numPlayers = int(numPlayers)
				converted = True

			except:
				numPlayers = raw_input("Please enter vaild input: ")
				converted = False

		#Adding the amount of players the user input
		for i in range(0, numPlayers):
			playerName = raw_input("Pleae give a name for player " + str(i) + ": ")
			self.players.append(player.Player(playerName))

		#Creating the house player for the other players to play against
		self.house = house.House()
	

	def runGame(self):
		self.setupGame()
		self.runPlayers()
		self.runResults()

	def setupGame(self):

		#looping through each of the players playing the game
		for p in self.players:
			#outputting the current players situation
			print("//////////////////////////////////////////////////////////////////////")
			print("Dealer deals " + p.name + " 2 cards")
			
			#dealing the player their initial cards
			p.setup(self.deck)

			p.showHandStatus()

			if p.isBust:
				print(p.name + " is out of the game, the house takes their money")


		print("//////////////////////////////////////////////////////////////////////")
		self.house.setup(self.deck)


	def runPlayers(self):

		#looping through each of the players playing the game
		for p in self.players:

			if p.isBust == False:
				#outputting the current players situation
				print("//////////////////////////////////////////////////////////////////////")
				print("It is " + p.name + "'s turn")

				print(p.name + "'s current hand is:")
				p.showHandStatus()

				playerInput = raw_input("Would you like to play this round? (Please answer with 'y' or 'n')")

				playerPlaying = self.checkPlayerResponse(playerInput)

				while playerPlaying:

					newCard = self.deck.dealCard()

					print("Dealer deals " + p.name)
					newCard.display()

					p.hitMe(newCard)
					print(p.name + "'s current hand is:")
					p.showHandStatus()

					if p.isBust:
						print(p.name + " went bust")
						playerPlaying = False

					else:
						playerInput = raw_input("Would you like another card? (Please answer with 'y' or 'n')")

						playerPlaying = self.checkPlayerResponse(playerInput)

		self.house.playTurn(self.deck)

	def runResults(self):
		print("//////////////////////////////////////////////////////////////////////")
		print("The game is over. The results are:")
		
		#looping through each of the players playing the game
		for p in self.players:
			#checking if the player went bust during the game
			if p.isBust:
				print(p.name + " went bust, the house took their money")
			else:
				if p.hand.getTotal() > self.house.hand.getTotal() or self.house.isBust:
					print(p.name + " beats the house, house pays out money")
				elif p.hand.getTotal() == self.house.hand.getTotal():
					print("Even between both " + p.name + " and " + self.house.name + " both keep their money")
				else:
					print(p.name + "'s hand has a lower value that " + self.house.name + ", " +  self.house.name + " takes their money")

	def checkPlayerResponse(self, playerInput):

		while playerInput not in self.VALID_INPUTS:
			playerInput = raw_input("Please enter vaild input: ")

		if playerInput is 'y' or playerInput is 'Y':
			return True
		else:
			return False


