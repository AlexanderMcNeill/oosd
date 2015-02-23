import deck
import card
import hand
import player
#import house
#testing
gameDeck = deck.Deck()

playerName = raw_input('Please enter your name? testing')

gamePlayer = player.Player(playerName) 

#gameHouse = house.House()

#gameHouse.setup(gameDeck)

gamePlayer.playTurn(gameDeck)

#gameHouse.playTurn(gameDeck)