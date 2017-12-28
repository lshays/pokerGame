from random import shuffle, random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'S', 'C']

deck = []
for card in cards:
    for suit in suits:
        deck.append(str(card) + suit)

def getDeck():
    shuffle(deck, random)
    return deck
    
def shuffleDeck(d):
    shuffle(d, random)
