i = 0
j = 0

for item in range(5):
    row = input().split()

    if "1" in row:
        i = item
        j = row.index("1")
    
print(abs((i - 2)) + abs(j - 2))