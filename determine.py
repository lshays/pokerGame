def royalFlush(hand):
    suitSet = set()
    cardSet = set()
    for card in hand:
        cardSet.add(card[0])
        suitSet.add(card[1])
    if cardSet.issuperset(set(["A", "K", "Q", "J", "T"])):
        if len(suitSet) == 1:
            return 10


def straightFlush(hand):
    suitSet = set()
    cardList = []
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        cardList.append(card[:-1])
        suitSet.add(card[-1])
    if len(suitSet) == 1:
        cardList = map(int, cardList)
        cardList = sorted(cardList)
        if sum([1 for i in range(len(cardList)-1) if cardList[i] == cardList[i+1]-1]) == 4:
            return 9.0 + max(cardList) / 100.0


def fourOfAKind(hand):
    cardDic = {}
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = int(card[:-1])
        if card not in cardDic:
            cardDic[card] = 1
        else:
            cardDic[card] += 1
    for key in cardDic:
        if cardDic[key] == 4:
            return 8.0 + key / 100.0 


def fullHouse(hand):
    # Does not account for four of a kind since four of a kind takes precedence
    cardDic = {}
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = int(card[:-1])
        if card not in cardDic:
            cardDic[card] = 1
        else:
            cardDic[card] += 1
    if len(cardDic) == 2:
        ret = 7.0
        for key in cardDic:
            if cardDic[key] == 3:
                ret += key / 100.0
            else:
                ret += key / 10000.0
        return ret


def flush(hand):
    suitSet = set()
    cardList = []
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        cardList.append(card[:-1])
        suitSet.add(card[-1])
    if len(suitSet) == 1:
        cardList = map(int, cardList)
        cardList = sorted(cardList)
        ret = 6.0
        x = 100.0
        while cardList:
            ret += cardList.pop() / x
            x *= 100.0
        return ret


def straight(hand):
    cardList = []
    for card in hand:
        card = card[:-1]
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        cardList.append(int(card))
    cardList = sorted(cardList)
    if sum([1 for i in range(len(cardList)-1) if cardList[i] == cardList[i+1]-1]) == 4:
        return 5.0 + max(cardList) / 100.0


def threeOfAKind(hand):
    cardList = []
    cardDic = {}
    for card in hand:
        card = card[:-1]
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = int(card)
        cardList.append(card)
        if card in cardDic:
            cardDic[card] += 1
        else:
            cardDic[card] = 1
    for key in cardDic:
        if cardDic[key] == 3:
            return 4.0 + key / 100.0


def twoPairs(hand):
    cardDic = {}
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = card[:-1]
        card = int(card)
        if card in cardDic:
            cardDic[card] += 1
        else:
            cardDic[card] = 1
    pairCards = []
    for key in cardDic:
        if cardDic[key] == 2:
            pairCards.append(key)
    if len(pairCards) == 2:
        last = 0
        for key in cardDic:
            if key not in pairCards:
                last = key
        return 3.0 + max(pairCards) / 100.0 + min(pairCards) / 10000.0 + last / 1000000.0


def onePair(hand):
    cardDic = {}
    cardList = []
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = card[:-1]
        card = int(card)
        cardList.append(card)
        if card in cardDic:
            cardDic[card] += 1
        else:
            cardDic[card] = 1
    ret = 0
    for key in cardDic:
        if cardDic[key] == 2:
            ret += 2.0 + key / 100.0
            cardList.remove(key)
            x = 10000.0
            while cardList:
                cardList = sorted(cardList)
                ret += cardList.pop() / x
                x *= 100.0
            return ret


def highCard(hand):
    cardList = []
    for card in hand:
        card = card.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")
        card = card[:-1]
        card = int(card)
        cardList.append(card)
    ret = 1.0
    x = 100.0
    cardList = sorted(cardList)
    while cardList:
        ret += cardList.pop() / x
        x *= 100.0
    return ret


def winner(p1Hand, p2Hand):
    possibleHands = []
    possibleHands.append((royalFlush, "Royal Flush"))
    possibleHands.append((straightFlush, "Straight Flush"))
    possibleHands.append((fourOfAKind, "Four of a Kind"))
    possibleHands.append((fullHouse, "Full House"))
    possibleHands.append((flush, "Flush"))
    possibleHands.append((straight, "Straight"))
    possibleHands.append((threeOfAKind, "Three of a Kind"))
    possibleHands.append((twoPairs, "Two Pairs"))
    possibleHands.append((onePair, "One Pair"))
    possibleHands.append((highCard, "High Card"))
    p1 = (0, "")
    p2 = (0, "")

    for hand in possibleHands:
        result = hand[0](p1Hand)
        if result:
            p1 = (result, hand[1])
            break
        
    for hand in possibleHands:
        result = hand[0](p2Hand)
        if result:
            p2 = (result, hand[1])
            break

    if p1[0] > p2[0]:
        return 1, p1[1], p2[1]
    if p2[0] > p1[0]:
        return 2, p1[1], p2[1]
    else:
        return 0, p1[1], p2[1]

def bestHand(p1Hand, p2Hand, middle):
    from itertools import permutations
    p1Hands = permutations(p1Hand + middle, 5)
    p2Hands = permutations(p2Hand + middle, 5)
    possibleHands = []
    possibleHands.append(royalFlush)
    possibleHands.append(straightFlush)
    possibleHands.append(fourOfAKind)
    possibleHands.append(fullHouse)
    possibleHands.append(flush)
    possibleHands.append(straight)
    possibleHands.append(threeOfAKind)
    possibleHands.append(twoPairs)
    possibleHands.append(onePair)
    possibleHands.append(highCard)

    p1Score = 0
    p2Score = 0
    for hand in p1Hands:
        for f in possibleHands:
            if f(hand) > p1Score:
                p1Score = f(hand)
                p1Hand = hand
            else:
                continue

    for hand in p2Hands:
        for f in possibleHands:
            if f(hand) > p2Score:
                p2Score = f(hand)
                p2Hand = hand

    return (p1Hand, p2Hand)


