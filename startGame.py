from generateHands import getHands
from determine import winner, bestHand
from printer import printCards

while True:
    hands = getHands()
    p1 = hands[0]
    p2 = hands[1]
    middle = hands[2] 

    temp = bestHand(p1, p2, middle)
    p1Final = temp[0]
    p2Final = temp[1]

    w = winner(p1Final, p2Final)
    
    printCards(p2, False, indented=True)
    printCards(middle, False)
    printCards(p1, True, indented=True)

    raw_input("...")
    print "\n"

    printCards(p2, message=w[2], indented=True)
    printCards(middle)
    printCards(p1, message=w[1], indented=True)
    
    if w[0] == 1:
        print "YOU WIN!!!"
    elif w[0] == 2:
        print "YOU'RE A LOSER! HAHAHA!"
    else:
        print "Wow, a tie."

    option = raw_input("Press Enter to play again, type 'q' to quit: ")
    if option.lower() == 'q':
        break
    print "\n"
