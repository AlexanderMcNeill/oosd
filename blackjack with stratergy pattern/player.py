import re
import hand
import player_strategy
import house_strategy

class Player:

    def __init__(self, strategy):
        self.hand = hand.Hand()
        self.strategy = strategy

    def take_card(self, cd):
        self.hand.add(cd)

    def show_hand(self):
        return str(self.hand) + " Score: " + str(self.hand.score())

    def hits(self):
        return self.strategy.hits(self.hand)

    def score(self):
        return self.hand.score()


class HousePlayer(Player):

    def hits(self):
        return self.strategy.hits(self.hand)

    def show_hand_hidden_down(self):
        cards = str(self.hand)
        #replace first card with '**'
        card_to_hide = re.compile("(^\w+)\s")
        return card_to_hide.sub("** ", cards)
