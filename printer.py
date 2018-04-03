# -*- coding: utf-8 -*-
"""
This module encapsulates the card printing functionality of the poker game.
It has been designed with windows and linux compatibilty in mind.

Todo:
    Check for cross platform compatibility.
"""
import os

if os.name == 'nt':
    # Windows
    SPADE = "\x06"
    CLUB = "\x05"
    HEART = "\x03"
    DIAMOND = "\x04"
else:
    # Linux
    SPADE = "\xE2\x99\xA0"
    CLUB = "\xE2\x99\xA3"
    HEART = "\xE2\x99\xA5"
    DIAMOND = "\xE2\x99\xA6"
"""
OS Dependent Hex codes for printing suits
"""

def getCard(c, s):
    """
    Gets list of strings that build specified card

    Args:
        c(str): The card to be displayed. ex: 8,9...K,A
        s(str): The suit of the card. (S,H,D,C)

    Returns:
        List of strings that builds card

    """
    s = s.replace("H", HEART)\
        .replace("C", CLUB)\
        .replace("D", DIAMOND)\
        .replace("S", SPADE)
    c = c.replace("T", "10")
    card = []
    card.append(u"┌─────────┐")
    card.append(u"|{0}       {1}|".format(c, s))
    card.append(u"|         |")
    card.append(u"|         |")
    card.append(u"|    {0}    |".format(c))
    card.append(u"|         |")
    card.append(u"|{1}       {0}|".format(c, s))
    card.append(u"└─────────┘")
    if c == "10": 
        # Adjust spacing for 10 card
        for i in range(len(card)):
            if c in card[i]:
                card[i] = card[i].replace(" ", "", 1)
    return card

def printCards(cards, faceUp=[1, 1, 1, 1, 1], message="", indented=False):
    """
    Prints a hand of cards and optional message to the screen.

    Args:
        cards(obj): Hand of cards to be printed
        faceUp(obj): List that maps what cards to be shown face up
            1 -> Face up
            0 -> Face down
            Default -> All Faceup
        message(str): Optional message to be displayed after row of cards
        indented(bool): Optional argument to indent the displayed cards

    """
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