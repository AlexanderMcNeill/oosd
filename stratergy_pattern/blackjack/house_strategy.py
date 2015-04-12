__author__ = 'alexmcneill'

import hand


class HouseStrategy():

    def __init__(self):
        pass

    def hits(self, hand):
        if hand.score() > 17:
            return False
        else:
            return True