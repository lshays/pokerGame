cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'S', 'C']

deck = []
for card in cards:
    for suit in suits:
        deck.append(str(card) + suit)

from random import shuffle, random
shuffle(deck, random) 

def getHands(holdem = True):
    shuffle(deck, random)
    if holdem:
        return(deck[0:2], deck[2:4], deck[4:9])
    return (deck[0:5], deck[5:10])

if __name__ == "__main__":
    hands = getHands()
    print "Player 1's hand:", hands[0]
    print "Player 2's hand:", hands[1]
