from generateHands import getHands
from determine import winner


def printCard(c, s):
    s = s.replace("H", "\xE2\x99\xA5").replace("C", "\xE2\x99\xA3").replace("D", "\xE2\x99\xA6").replace("S", "\xE2\x99\xA0")
    c = c.replace("T", "10")
    card = []
    card.append(" _________ ")
    card.append("|{0}       {1}|".format(c, s))
    card.append("|         |")
    card.append("|         |")
    card.append("|    {0}    |".format(c))
    card.append("|         |")
    card.append("|{1}       {0}|".format(c, s))
    card.append(" --------- ")
    for i in range(len(card)):
        if c == "10" and c in card[i]:
            index = card[i].index(" ")
            card[i] = card[i][:index] + card[i][index+1:]
    return card


while True:
    hands = getHands()
    p1 = hands[0]
    p2 = hands[1]

    w = winner(p1, p2)[0]
    
    handString = [] 
    for card in p2:
        for i in range(len(printCard(" ", " "))):
            handString.append("")
            handString[i] += printCard(" ", " ")[i]
    for line in handString:
        if line:
            print line
    handString = []
    for card in p1:
        for i in range(len(printCard(card[0], card[1]))):
            handString.append("")
            handString[i] += printCard(card[0], card[1])[i]
    for line in handString:
        if line:
            print line

    raw_input("...")
    print "\n"

    handString = []
    for card in p2:
        for i in range(len(printCard(card[0], card[1]))):
            handString.append("")
            handString[i] += printCard(card[0], card[1])[i]
    for line in handString:
        if line:
            if len(line.replace(" ", "").replace('|', ' ')) >= 15 and len(line.replace(" ", "").replace('|', ' ')) <= 20:
                print line, winner(p1, p2)[2]
            else:
                print line
    handString = []
    for card in p1:
        for i in range(len(printCard(card[0], card[1]))):
            handString.append("")
            handString[i] += printCard(card[0], card[1])[i]
    for line in handString:
        if line:
            if len(line.replace(" ", "").replace('|', ' ')) >= 15 and len(line.replace(" ", "").replace('|', ' ')) <= 20: 
                print line, winner(p1, p2)[1]
            else:
                print line

    if w == 1:
        print "YOU WIN!!!"
    elif w == 2:
        print "YOU'RE A LOSER! HAHAHA!"
    else:
        print "Wow, a tie."

    option = raw_input("Press Enter to play again, type 'q' to quit: ")
    if option.lower() == 'q':
        break
    print "\n"
