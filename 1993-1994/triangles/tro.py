n = int(input(""))

if not (3 <= n <= 10000):
    print("Musisz podać co najmniej 3 odcinki i nie więcej niż 10000 odcinków!")
else:
    
    odcinek = []

    for i in range(n):
        linia = input("")
        
        a,b = linia.split("/")
        a = int(a)
        b = int(b)
        
        odcinek.append(a/b)
        odcinek.sort()

    if odcinek[0] + odcinek[1] > odcinek[-1]:
        print("TAK")
    else:
        print("NIE")