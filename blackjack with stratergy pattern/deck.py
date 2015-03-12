import card
import random
import random_pos_shuffle
import evens_odds_shuffle
import random_class_shuffle

class Deck:


    def __init__(self, shuffle_method):
        self.cards = []
        for suit in "CDHS":
            for val in range(1, 11):
                self.cards.append(card.Card(val, suit))
            for val in "AKQJ":
                self.cards.append(card.Card(val, suit))
        self.shuffle_method = shuffle_method
        
    def shuffle(self):
        self.shuffle_method.shuffle(self.cards)

    def get_card_name(self, index):
        card = self.cards[index]
        return str(card.value) + card.suit

    def next(self):
        return self.cards.pop()
        



