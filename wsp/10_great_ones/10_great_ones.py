liczba_kandydatów = int(input(""))

if (1 <= liczba_kandydatów <= 1000000):
    moce = list(map(int, input("").split()))
    
    if not (-1000000 <= max(moce) <= 1000000):
        print("Moc kandydata musi być z zakresu od -1000000 do 1000000")
    else:
        sortowane = sorted(moce, reverse=True)[:10]
        print(*sortowane)
