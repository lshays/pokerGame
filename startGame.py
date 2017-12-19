from generateHands import getHands
from determine import winner, bestHand
from printer import printCards

def placeBet(chips):
    bet = raw_input("<Enter> = pass, <f> = fold\nEnter number of chips to bet: ")
    if not bet:
        return
    else:
        try:
            if bet.lower() == "f":
                return bet
            bet = int(bet)
            if bet > chips:
                print "Oops, you dont have that many chips silly!"
                placeBet(chips)
            else:
                return bet
        except ValueError:
            print "Oops, you can't bet {0} chips silly!".format(bet) 
            placeBet(chips)

chips = 100
while True:
    hands = getHands()
    p1 = hands[0]
    p2 = hands[1]
    middle = hands[2] 
    pot = 10
    chips -= 5

    temp = bestHand(p1, p2, middle)
    p1Final = temp[0]
    p2Final = temp[1]

    w = list(winner(p1Final, p2Final))
    
    printCards(p2, [0, 0], indented=True)
    printCards(middle, [0, 0, 0, 0, 0], message="Pot: " + str(pot))
    printCards(p1, indented=True)
    print "Chips:", chips

    fold = False
    bet = placeBet(chips)
    if bet:
        if bet == "f":
            fold = True
            w[0] = 2
            w[2] = ""
        else:
            chips -= bet
            pot += 2*bet
    print "\n"

    if not fold:
        faceUp = [1, 1, 0, 0, 0]
        while not all(faceUp):
            for x in range(len(faceUp)):
                if faceUp[x] == 0:
                    faceUp[x] = 1
                    break
            printCards(p2, [0, 0], indented=True)
            printCards(middle, faceUp, message="Pot: " + str(pot))
            printCards(p1, indented=True)
            print "Chips:", chips
            bet = placeBet(chips)
            if bet:
                if bet == "f":
                    fold = True
                    w[0] = 2
                    w[2] = ""
                    break
                chips -= bet
                pot += 2*bet
            print "\n"

    printCards(p2, [not fold, not fold], message=w[2], indented=True)
    printCards(middle, message="Pot: " + str(pot))
    printCards(p1, message=w[1], indented=True)
    
    if w[0] == 1:
        print "YOU WIN!!!"
        chips += pot
    elif w[0] == 2:
        print "YOU'RE A LOSER! HAHAHA!"
        if chips == 0:
            print "You're out of chips, better luck next time..."
            break
    else:
        print "Wow, a tie."
        chips += pot/2
    print "Chips", chips

    option = raw_input("Press Enter to play again, type 'q' to cashout: ")
    if option.lower() == 'q':
        break
    print "\n"
