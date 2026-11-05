import random

def pokersimulation():
    gezogeneKarten = getRandom()
    if checkRoyalFlush(gezogeneKarten):
        return 1
    if checkStraightFlush(gezogeneKarten):
        return 2

    if checkFlush(gezogeneKarten):
        return 5
    if checkStraight(gezogeneKarten):
        return 6

    return 10

def checkRoyalFlush(gezogeneKarten):
    if checkFlush(gezogeneKarten) is False:
        return False
    if checkStraight(gezogeneKarten) is False:
        return False
    checkAssUKing = []
    for karten in gezogeneKarten:
        x = karten%13
        if x == 12 or x == 11:
            checkAssUKing.append(x)
    if 12 in checkAssUKing and 11 in checkAssUKing:
        return True

def checkStraightFlush(gezogeneKarten):
    if checkFlush(gezogeneKarten) is False:
        return False
    if checkStraight(gezogeneKarten) is False:
        return False
    return True


def checkFlush(gezogeneKarten):
    farben = []
    
    for i in gezogeneKarten:
        x = i // 13
        farben.append(x)
    for farbe in farben:
        if farben[0] != farbe:
            return False
    return True

def checkStraight(gezogeneKarten):
    zahl = []

    for i in gezogeneKarten:
        x = i%13
        zahl.append(x)
    zahl.sort()

    if zahl == [0, 1, 2, 3, 12]:
        return True

    for i in range(4):
        if zahl[i] + 1 != zahl[i + 1]:
            return False

    return True

def getRandom():
    karten = list(range(1,52))
    gezogene_karte = []

    for i in range(5):
        laenge = len(karten)
        idx = random.randint(0, laenge - i -1)
        zahl = karten[idx]
        letzterIndex = laenge - i -1

        karten[idx],karten[letzterIndex] = karten[letzterIndex],karten[idx]
        gezogene_karte.append(zahl)

    return gezogene_karte





if __name__ == "__main__":
    pass