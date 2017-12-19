# -*- coding: utf-8 -*-
# ^^^ Allows characters such as suit representations to be used in code

def getCard(c, s):
    s = s.replace("H", "♥").replace("C", "♣").replace("D", "♦").replace("S", "♠")
    c = c.replace("T", "10")
    card = []
    card.append("┌─────────┐")
    card.append("|{0}       {1}|".format(c, s))
    card.append("|         |")
    card.append("|         |")
    card.append("|    {0}    |".format(c))
    card.append("|         |")
    card.append("|{1}       {0}|".format(c, s))
    card.append("└─────────┘")
    for i in range(len(card)):
        if c == "10" and c in card[i]:
            index = card[i].index(" ")
            card[i] = card[i][:index] + card[i][index+1:]
    return card


def printCards(cards, faceUp=True, message="", indented=False):
    lines = []
    if indented:
        lines = ["\t\t" for i in range(8)]
    else:
        lines = ["" for i in range(8)]
    for card in cards:
        if faceUp:
            cardLines = getCard(card[:-1], card[-1])
        else:
            cardLines = getCard(" ", " ")
        for i in range(len(cardLines)):
            lines[i] += cardLines[i]
    lines[4] += "\t" + message
    for line in lines:
        print line

