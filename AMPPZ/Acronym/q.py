n = int(input())

words = []

for _ in range(n):
    words.append(input().strip())

first_letters = {}

for word in words:
    first_char = word[0]

    if first_char not in first_letters:
        first_letters[first_char] = word

found = False

for acronym in words:
    can_make = True
    sentence = []

    for char in acronym:
        
        if char in first_letters:
            sentence.append(first_letters[char])
        else:
            can_make = False
            break

    if can_make:
        print(len(sentence))
        print(" ".join(sentence))
        found = True
        break

if not found:
    print(-1)