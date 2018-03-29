# -*- coding: utf-8 -*-
import os

if os.name == 'nt': # Windows
    SPADE = "\x06"
    CLUB = "\x05"
    HEART = "\x03"
    DIAMOND = "\x04"
else: # Linux
    SPADE = "\xE2\x99\xA0"
    CLUB = "\xE2\x99\xA3"
    HEART = "\xE2\x99\xA5"
    DIAMOND = "\xE2\x99\xA6"


# Input:
    # c - The numeric value of the card (2,3,4...Q,K,A)
    # s - The suit of the card
# Output: 
    # card - A list of strings that represent a printable card
# Effect:
    # void
def getCard(c, s):
    s = s.replace("H", HEART).replace("C", CLUB).replace("D", DIAMOND).replace("S", SPADE)
    c = c.replace("T", "10")
    card = []
    card.append(u"┌─────────┐")
    card.append("|{0}       {1}|".format(c, s))
    card.append("|         |")
    card.append("|         |")
    card.append("|    {0}    |".format(c))
    card.append("|         |")
    card.append("|{1}       {0}|".format(c, s))
    card.append(u"└─────────┘")
    if c == "10": # Adjust spacing for 10 card
        for i in range(len(card)):
            if c in card[i]:
                card[i] = card[i].replace(" ", "", 1)
    return card


# Input:
    # cards - card objects
    # faceUp - which cards should be shown faceUp (1=faceup)
    # message - message to be printed after cards displayed (winner, loser, etc) 
    # indented - Shifts card display to right
# Output:
    # void
# Effect:
    # Hand of cards + optional message printed to screen
def printCards(cards, faceUp=[1, 1, 1, 1, 1], message="", indented=False):
    lines = []
    if indented:
        lines = ["\t\t" for i in range(8)]
    else:
        lines = ["" for i in range(8)]
    for x in range(len(cards)):
        if faceUp[x]:
            cardLines = getCard(cards[x][:-1], cards[x][-1])
        else:
            cardLines = getCard(" ", " ")
        for i in range(len(cardLines)):
            lines[i] += cardLines[i]
    lines[4] += "\t" + message
    for line in lines:
        print line