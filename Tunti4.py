def jakoyhtälö():
    jaettava = int(input("Anna jaettava: "))
    jakaja = int(input("Anna jakaja: "))
    print(f"Jakolaskun osmäärä on {jaettava // jakaja} ja jakolaskun jakojäännös on {jaettava % jakaja}")


def suorakulmainen():
    a, b, c = 3, 4, 5
    if a**2 + b**2 == c**2:
        print("Kolmio on suorakulmainen")
    else:
        print("Komlio ei ole suorakulmainen")


def aritmeetinen():
    alku = 7
    kerroin = 5
    summa = 0
    laskut = 0

    for x in range(10):
        summa += alku + kerroin * x
        print(alku + kerroin * x, end=", ")
    print(f"ja niiden summa on {summa}")

    summa = 0
    while summa < 1000:
        summa += alku + kerroin * x
        laskut += 1
    print(f"On laskettava {laskut}, että summa ylitää 1000")


def jaolliset():
    for x in range(1, 101): x if x % 3 != 0 else print(x, end=", ")


def summa():
    summa = []
    for i in range(1, 100): i if i % 2 == 0 else summa.append(i)
    print(f"lukujen summa on {sum(summa)}")


def arvoitus():
    for x in range(1, 100):
        if (x + 1) * (x - 3) * x == 47804:
            print(f"Bertan ikä on {x} vuotta")
            break


def yhtälön_ratkaisu():
    toteutuuko = -1
    for x in range(1, 100):
        if 2 * (x**3) - 172 * (x**2) - 288 * x + 199808 == 0:
            toteutuuko = x
    if toteutuuko < 0:
        print("yhtälö ei toteudu")
    else:
        print(f"Kokonaisluku on {toteutuuko}")


def nollakohdat():
    a = float(input("Anna a:n arvo: "))
    b = float(input("Anna b:n arvo: "))
    c = float(input("Anna c:n arvo: "))
    if b ** 2 - 4 * a * c > 0:
        print("yhtälöllä on kaksi nollakohtaa")
    elif b ** 2 - 4 * a * c == 0:
        print("yhtälöllä on yksi nollakohtaa")
    else:
        print("yhtälöllä ei ole yhtään nollakohtia")


def noppa():
    määrä = 0
    for x in range(1, 7):
        for y in range(1, 7):
            for z in range(1, 7):
                if x + y + z == 8:
                    määrä += 1
    print(f"Summan kahdeksan voi saada {määrä} tavalla")

def main():
    # jakoyhtälö()
    # suorakulmainen()
    # aritmeetinen()
    # jaolliset()
    # summa()
    # arvoitus()
    # yhtälön_ratkaisu()
    # nollakohdat()
    noppa()


main()