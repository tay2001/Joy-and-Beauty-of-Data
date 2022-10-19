import Deck

cards = Deck.deck()
cards.print_deck()

cards.shuffle()
print("After shuffling...\n")
cards.print_deck()
