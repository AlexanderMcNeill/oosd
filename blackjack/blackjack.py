import deck
import card
import hand
import player
import house

gameDeck = deck.Deck()

playerName = raw_input('Please enter your name? ')

gamePlayer = player.Player(playerName) 

gameHouse = house.House()


gameHouse.setup(gameDeck)

gamePlayer.playTurn(gameDeck)

if gamePlayer.bust == False:
	gameHouse.playTurn(gameDeck)

	if gameHouse.bust == False:

		houseTotal = gameHouse.playerHand.getTotal()
		playerTotal =  gamePlayer.playerHand.getTotal()

		if houseTotal > playerTotal:
			print("House wins")
		elif houseTotal == playerTotal:
			print("No one wins")
		else:
			print(gamePlayer.playerName + " wins")
	else:
		print(gamePlayer.playerName + " wins")

elif gameHouse.bust == True:
	print("No one wins")
else:
	print("House wins")
