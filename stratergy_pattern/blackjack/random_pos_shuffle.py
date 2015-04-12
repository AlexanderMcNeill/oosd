__author__ = 'alexmcneill'

import random


class RandomPosShuffle():

    def __init__(self):
        pass

    def shuffle(self, cards):
        for i in range(0, len(cards)):
            card_index_one = random.randrange(0, len(cards))
            card_index_two = random.randrange(0, len(cards))

            temp = cards[card_index_one]
            cards[card_index_one] = cards[card_index_two]
            cards[card_index_two] = temp