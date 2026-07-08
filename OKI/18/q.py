how_many_commands = int(input())

increases = []

for _ in range(how_many_commands):
    command = input().split()

    if command[0] == "z":
        increases.append(int(command[1]))
    
    elif command[0] == "u":
        try:
            increases.remove(int(command[1]))
        
        except ValueError:
            pass
    
    elif command[0] == "r":
        if len(increases) == 0:
            print("PUSTO!")
        
        else:
            print(max(increases) - min(increases))