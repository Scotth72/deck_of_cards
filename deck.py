import itertools
import random

# create card deck
cards = []
suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
royal_cards = ["J", "Q", "K", "A"]
deck_of_cards = []

for card in range(2, 11):
    cards.append(str(card))

for royal_card in range(4):
    cards.append(royal_cards[royal_card])

for r_card in range(4):
    for num_cards in range(13):
        card = (cards[num_cards] + " of " + suites[r_card]) 
        deck_of_cards.append(card)

print(deck_of_cards)


# need to shuffle the card deck

random.shuffle(deck_of_cards)

for random_deck in range(52):
    print(deck_of_cards[random_deck])