n = int(input(""))

if not (3 <= n <= 10000):
    print("You must provide at least 3 segments and no more than 10000 segments!")
else:
    segments = []

    for i in range(n):
        line = input("")
        
        a, b = line.split("/")
        a = int(a)
        b = int(b)
        
        segments.append(a / b)
    
    segments.sort()

    if segments[0] + segments[1] > segments[-1]:
        print("YES")
    else:
        print("NO")
