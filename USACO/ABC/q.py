number = list(map(int, input().split()))
number.sort()

a = int(number[0])
b = int(number[1])
c = int(number[-1]) - a - b

print(a, b, c)