if __name__ == '__main__':
    # Read the integers n and m
    n, m = map(int, input().split())
    
    # Read the array of n integers
    array = list(map(int, input().split()))
    
    # Read set A of m integers
    A = set(map(int, input().split()))
    
    # Read set B of m integers
    B = set(map(int, input().split()))
    
    # Initialize happiness
    happiness = 0
    
    # Calculate happiness
    for num in array:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    
    # Output the final happiness
    print(happiness)
