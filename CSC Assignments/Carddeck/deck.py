import card
import random

class Deck:
    """Deck class for representing and manipulating 52 instances of Card"""
    def __init__(self):
        """A constructor method that creates a 52 card deck"""
        self.cards = []
        for rank in ["two", "three", "four", "five", "six", "seven", "eight",
                     "nine", "ten", "jack", "queen", "king", "ace"]:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                self.cards += [card.Card(rank,suit)]

    def print_deck(self):
        """A method that prints the 52 card deck"""
        print("Deck of Cards")
        print("-------------")
        number = 1
        for card in self.cards:
            print(number, card)
            number += 1
        print()

    def shuffle2(self):
        shuffled = []
        while self.cards != []:
            pos = random.randint(0, len(self.cards) - 1)
            remove = self.cards[pos]
            shuffled += [remove]
            self.cards.remove(remove)
        self.cards = shuffled

    def shuffle(self):
        random.shuffle(self.cards)



        


