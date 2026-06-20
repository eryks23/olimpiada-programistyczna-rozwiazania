candidate_count = int(input(""))

if 1 <= candidate_count <= 1000000:
    powers = list(map(int, input("").split()))
    
    if not (-1000000 <= max(powers) <= 1000000):
        print("Candidate power must be within the range of -1000000 to 1000000")
    else:
        sorted_powers = sorted(powers, reverse=True)[:10]
        print(*sorted_powers)
