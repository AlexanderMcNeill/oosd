__author__ = 'alexmcneill'

import deck
import math
import random_class_shuffle
import random_pos_shuffle
import evens_odds_shuffle

def init_result(result):
    for suit in "CDHS":
        for val in range(1, 11):
            result[(str(val) + suit)] = [0] * 52
        for val in "AKQJ":
            result[(str(val) + suit)] = [0] * 52

def test_deck(deck, result):
    for i in range(0, 520):
        deck.shuffle()
        for j in range(0, 52):
            result[deck.get_card_name(j)][j] += 1

def analyse_results(results, name):
    result = 0

    for suit in "CDHS":
        for val in range(1, 11):
            for j in range(0, 52):
                current_val = results[(str(val) + suit)][j]
                result += math.pow((current_val - 10), 2) / 10
        for val in "AKQJ":
            for j in range(0, 52):
                current_val = results[(str(val) + suit)][j]
                result +=  math.pow((current_val - 10), 2) / 10

    print (name + " scored " + str(result) + " on the chi-squared test")

d1_results = {}
init_result(d1_results)

d1 = deck.Deck(random_class_shuffle.RandomClassShuffle())
test_deck(d1, d1_results)

analyse_results(d1_results, "Shuffle class shuffle")

d2_results = {}
init_result(d2_results)

d2 = deck.Deck(evens_odds_shuffle.EvensOddsShuffle())
test_deck(d2, d2_results)

analyse_results(d2_results, "Odds and Evens shuffle")

d3_results = {}
init_result(d3_results)

d3 = deck.Deck(random_pos_shuffle.RandomPosShuffle())
test_deck(d3, d3_results)

analyse_results(d3_results, "Random Position Shuffle")