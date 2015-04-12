__author__ = 'alexmcneill'

import hand

class PlayerStrategy():

    def __init__(self):
        pass

    def hits(self, hand):
        return raw_input("(h)it or (s)tand: ") == "h"