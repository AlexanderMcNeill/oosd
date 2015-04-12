__author__ = 'alexmcneill'
import hand

class PlayerStratergy():


    def __init__(self):
        pass

    def checkPlayerResponse(self, playerInput):

        while playerInput not in self.VALID_INPUTS:
            playerInput = raw_input("Please enter vaild input: ")

        if playerInput is 'y' or playerInput is 'Y':
            return True
        else:
            return False

    def hits(self, hand):
        player_input = raw_input("Would you like to play this round? (Please answer with 'y' or 'n')")
        hit = self.checkPlayerResponse(player_input)
        return hit