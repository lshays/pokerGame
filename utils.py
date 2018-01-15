def placeBet(chips):
    bet = raw_input("Enter number of chips to bet: ")
    try:
        bet = int(bet)
        if bet > chips:
            print "Oops, you dont have that many chips silly!"
            return placeBet(chips)
        if bet < 0:
            print "You can't bet negative chips dumb dumb!"
            return placeBet(chips)
        else:
            return bet
    except ValueError:
        print "Oops, you can't bet {0} chips silly!".format(bet) 
        return placeBet(chips)
            
def raiseBet(currentBet, chips):
    bet = raw_input("Current bet is {0}, how much would you like to raise by: ".format(currentBet))
    try:
        bet = int(bet)
        if bet < 0:
            print "You can't bet negative chips dumb dumb!"
            return raiseBet(currentBet, chips)
        bet += currentBet
        if bet > chips:
            print "Oops, you dont have that many chips silly!"
            return raiseBet(currentBet, chips)
        else:
            return bet
    except ValueError:
        print "Oops, you can't bet {0} chips silly!".format(bet) 
        return raiseBet(currentBet, chips)
