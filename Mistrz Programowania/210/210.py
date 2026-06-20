number = int(input(""))

if (0 <= number <= 10**18):
    binary = bin(number)[2:]
    
    for element in binary:
        result = sum(int(element) for element in binary)
        binary_result = bin(result)[2:]
    
    print(binary, binary_result)
