import random

#Führt die Pokersimulation durch und gibt die statistik zurück
def pokersimulation(anzahl : int) -> dict[str, int]:
    ergebnisse = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Drilling": 0,
        "Two Pair": 0,
        "Pair": 0,
        "High Card": 0
    }

    for i in range(anzahl):
        gezogeneKarten = getRandom()
        if checkRoyalFlush(gezogeneKarten):
            hand = "Royal Flush"
        elif checkStraightFlush(gezogeneKarten):
            hand = "Straight Flush"
        elif checkSameCard(gezogeneKarten, 4):
            hand = "Vierling"
        elif checkFullHouse(gezogeneKarten):
            hand = "Full House"
        elif checkFlush(gezogeneKarten):
            hand = "Flush"
        elif checkStraight(gezogeneKarten):
            hand = "Straight"
        elif checkSameCard(gezogeneKarten, 3):
            hand = "Drilling"
        elif checkTwoPair(gezogeneKarten):
            hand = "Two Pair"
        elif checkSameCard(gezogeneKarten, 2):
            hand = "Pair"
        else:
            hand = "High Card"

        ergebnisse[hand] += 1

    return ergebnisse

#Checkt ob in der Hand eine Royal Flush vorhanden ist
def checkRoyalFlush(gezogeneKarten : list[int]) -> bool:
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
    return False

#Checkt ob in der Hand eine Straight Flush vorhanden ist
def checkStraightFlush(gezogeneKarten : list[int]) -> bool:
    if checkFlush(gezogeneKarten) is False:
        return False
    if checkStraight(gezogeneKarten) is False:
        return False
    return True

#Checkt ob in der Hand eine Flush vorhanden ist
def checkFlush(gezogeneKarten : list[int]) -> bool:
    farben = []
    
    for i in gezogeneKarten:
        x = i // 13
        farben.append(x)
    for farbe in farben:
        if farben[0] != farbe:
            return False
    return True

#Checkt ob in der Hand eine Straight vorhanden ist
def checkStraight(gezogeneKarten : list[int]) -> bool:
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

#Gibt 5 gezogene Karten zurück, die zufällig aus einem Kartendeck gezogen wurden
def getRandom() -> list[int]:
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

#Checkt ob in der Hand eine bestimmte Anzahl an gleichen Karten vorhanden ist
def checkSameCard(gezogeneKarten : list[int], Anzahl : int) -> bool:
    numbers = [karte % 13 for karte in gezogeneKarten]
    return any(numbers.count(number) == Anzahl for number in numbers)

#Checkt ob in der Hand ein Full House vorhanden ist
def checkFullHouse(gezogeneKarten : list[int]) -> bool:
    return checkSameCard(gezogeneKarten, 3) and checkSameCard(gezogeneKarten, 2)

#Checkt ob in der Hand zwei Paare vorhanden sind
def checkTwoPair(gezogeneKarten : list[int]) -> bool:
    zahlen = [karte % 13 for karte in gezogeneKarten]
    paare = sum(zahlen.count(zahl) == 2 for zahl in set(zahlen))
    return paare == 2



if __name__ == "__main__":
    anzahl = 1000000
    ergebnisse = pokersimulation(anzahl)
    for hand, count in ergebnisse.items():
        prozent = (count / anzahl) * 100
        print(f"{hand}: {count} ({prozent:.4f}%)")