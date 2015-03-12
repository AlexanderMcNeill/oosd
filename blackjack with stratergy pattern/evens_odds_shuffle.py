__author__ = 'alexmcneill'

import random


class EvensOddsShuffle():

    def __init__(self):
        pass

    def shuffle(self, cards):
        count = 0

        for evenIndex in range(0, len(cards), 2):
            oddIndex = random.randrange(0, len(cards), 3)

            temp = cards[oddIndex]
            cards[oddIndex] = cards[evenIndex]
            cards[evenIndex] = temp
