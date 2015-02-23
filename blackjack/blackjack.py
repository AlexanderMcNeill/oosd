import deck
import card
import hand
import player
#import house

gameDeck = deck.Deck()

playerName = raw_input('Please enter your name? ')

gamePlayer = player.Player(playerName) 

#gameHouse = house.House()

#gameHouse.setup(gameDeck)

gamePlayer.playTurn(gameDeck)

#gameHouse.playTurn(gameDeck)