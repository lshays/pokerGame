from determine import winner, bestHand
from printer import printCards
from client import Client
import sys

chips = 100
player = Client()

while True:
    player.newGame()
    print "Registering..."
    if not player.register():
        sys.exit()
    player.startGame()
    middle = player.getSharedCards()
    p1 = player.getHand()
    p2 = player.getOtherHands()[0]
    
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
    chipResult = player.placeBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    chipResult = player.placeSecondBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    pot = player.getPot()
    
    printCards(p2, [0, 0], indented=True)
    printCards(middle, [1, 1, 1, 0, 0], message="Pot: " + str(pot))
    printCards(p1, indented=True)
    print "Chips:", chips
    chipResult = player.placeBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    chipResult = player.placeSecondBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    pot = player.getPot()
    
    printCards(p2, [0, 0], indented=True)
    printCards(middle, [1, 1, 1, 1, 0], message="Pot: " + str(pot))
    printCards(p1, indented=True)
    print "Chips:", chips
    chipResult = player.placeBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    chipResult = player.placeSecondBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    pot = player.getPot()
    
    printCards(p2, [0, 0], indented=True)
    printCards(middle, [1, 1, 1, 1, 1], message="Pot: " + str(pot))
    printCards(p1, indented=True)
    print "Chips:", chips
    chipResult = player.placeBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    chipResult = player.placeSecondBet(chips)
    if chipResult == -1:
        w[0] = 2
    elif chipResult == -69:
        w[0] = 1
    else:
        chips -= chipResult
    pot = player.getPot()

    printCards(p2, [1, 1], message=w[2], indented=True)
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
