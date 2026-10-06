import random

def lottoziehung():
    zahlen = list(range(1, 46))
    gezogene_zahlen = []

    for i in range(6):
        laenge = len(zahlen)
        idx = random.randint(0, laenge - i - 1)
        zahl = zahlen[idx]
        letzter_index = laenge - i - 1

        zahlen[idx], zahlen[letzter_index] = zahlen[letzter_index], zahlen[idx]
        gezogene_zahlen.append(zahl)

    return gezogene_zahlen

def lottostatistik(anzahl_ziehungen):
    zahlen_dict = {i: 0 for i in range(1, 46)}
    for i in range(anzahl_ziehungen):
        gezogene_zahlen = lottoziehung()

        for zahl in gezogene_zahlen:
            zahlen_dict[zahl] += 1
    return zahlen_dict

if __name__ == "__main__":
    anzahl = input("Geben Sie die Anzahl der Ziehungen ein: ")
    gezogene_zahlen = lottostatistik(int(anzahl))
    print(f"Häufigkeit der gezogenen Lottozahlen nach {anzahl} Ziehungen:")
    for zahl, haeufigkeit in gezogene_zahlen.items():
        print(f"Zahl {zahl}: {haeufigkeit} mal gezogen")
    max = 0
    zahl_max = 0
    for zahl, haeufigkeit in gezogene_zahlen.items():
        if haeufigkeit > max:
            max = haeufigkeit
            zahl_max = zahl

    print(f"Die am häufigsten gezogene Zahl ist {zahl_max} mit {max} Ziehungen.")
