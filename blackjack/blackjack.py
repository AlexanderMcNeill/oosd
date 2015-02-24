import deck
import player
import house

	class Player(object):
		def __init__(self):
			self.deck = deck.Deck()
			self.players = []
			self.house = house.House()

		def setupPLayers(self):
			numPlayers = input("How many players? (max players 5)")

			while checkValidPlayerInput(numPlayers) == False:
				numPlayers = input("Please enter valid input. How many players? (max players 5)")

			for i in range(0, numPlayers):
				playerName = input("Pleae give a name for player " + str(i))
				self.players.append(player.Player(playerName))

		def checkValidPlayerInput(numPlayers):
			if numPlayers is int:
				if numPlayers < 6 and numPlayers > 0:
					return True
				else:
					return False
			else:
				return False

		def runGame(self):
			self.setupGame()
			self.runPlayers()
			self.runResults

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

			self.house.setup()
			self.house.showInitalHand()


		def runPlayers(self):

			#looping through each of the players playing the game
			for p in self.players

				if p.isBust = False:
					#outputting the current players situation
					print("//////////////////////////////////////////////////////////////////////")
					print("It is " + p.name + "'s turn")

					print(p.name + "'s current hand is:")
					p.showHandStatus()

					playerInput = input("Would you like to play this round? (Please answer with 'y' or 'n')")

					playerPlaying = self.checkPlayerResponse(playerInput)

					while playerPlaying:

						

						newCard = self.deck.dealCard()

						print("Dealer deals " + p.name " the " + newCard.display())

						print(p.name + "'s current hand is:")
						p.showHandStatus()

						if player.isBust:
							print(p.name + " went bust")
							playerPlaying = False

						else:
							playerInput = input("Would you like another card? (Please answer with 'y' or 'n')")

							playerPlaying = self.checkPlayerResponse(playerInput)

				self.house.playTurn(self.deck)

		def runResults():
			print("//////////////////////////////////////////////////////////////////////")
			print("The game is over. The results are:")
			
			#looping through each of the players playing the game
			for p in self.players:
				#checking if the player went bust during the game
				if p.isBust:
					print(p.name + " went bust, the house took their money")
				else:
					if p.hand.getTotal() > self.house.getTotal() or self.house.isBust:
						print(p.name + " beats the house, house pays out money")

		def checkPlayerResponse(self, playerInput):
			while playerInput is not 'y' or playerInput is not 'n':
				print("Please enter valid answer ('y' or 'n')")

			if playerInput is 'y' or playerInput is 'Y'
				return True
			else
				return False


