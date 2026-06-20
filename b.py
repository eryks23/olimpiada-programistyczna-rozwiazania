liczba = int(input(""))
if (0 <= liczba <= 10**18):
    binarna = bin(liczba)[2:]

    for element in binarna:
        wynik = sum(int(element) for element in binarna)

        wynik_binarna = bin(wynik)[2:]

    print(binarna, wynik_binarna)