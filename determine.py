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
    p1 = (0, "")
    p2 = (0, "")
    if royalFlush(p1Hand):
        p1 = (royalFlush(p1Hand), "Royal Flush")
    elif straightFlush(p1Hand):
        p1 = (straightFlush(p1Hand), "Straight Flush")
    elif fourOfAKind(p1Hand):
        p1 = (fourOfAKind(p1Hand), "Four of a Kind")
    elif fullHouse(p1Hand):
        p1 = (fullHouse(p1Hand), "Full House")
    elif flush(p1Hand):
        p1 = (flush(p1Hand), "Flush")
    elif straight(p1Hand):
        p1 = (straight(p1Hand), "Straight")
    elif threeOfAKind(p1Hand):
        p1 = (threeOfAKind(p1Hand), "Three of a Kind")
    elif twoPairs(p1Hand):
        p1 = (twoPairs(p1Hand), "Two Pairs")
    elif onePair(p1Hand):
        p1 = (onePair(p1Hand), "One Pair")
    else:
        p1 = (highCard(p1Hand), "High Card")

    if royalFlush(p2Hand):
        p2 = (royalFlush(p2Hand), "Royal Flush")
    elif straightFlush(p2Hand):
        p2 = (straightFlush(p2Hand), "Straight Flush")
    elif fourOfAKind(p2Hand):
        p2 = (fourOfAKind(p2Hand), "Four of a Kind")
    elif fullHouse(p2Hand):
        p2 = (fullHouse(p2Hand), "Full House")
    elif flush(p2Hand):
        p2 = (flush(p2Hand), "Flush")
    elif straight(p2Hand):
        p2 = (straight(p2Hand), "Straight")
    elif threeOfAKind(p2Hand):
        p2 = (threeOfAKind(p2Hand), "Three of a Kind")
    elif twoPairs(p2Hand):
        p2 = (twoPairs(p2Hand), "Two Pairs")
    elif onePair(p2Hand):
        p2 = (onePair(p2Hand), "One Pair")
    else:
        p2 = (highCard(p2Hand), "High Card")

    if p1[0] > p2[0]:
        return 1, p1[1], p2[1]
    if p2[0] > p1[0]:
        return 2, p1[1], p2[1]
    else:
        return 0, p1[1], p2[1]
