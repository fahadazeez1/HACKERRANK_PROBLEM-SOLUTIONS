# Python solution file --->
def symmetric_difference(a, b):
    # Convert lists to sets
    set_a = set(a)
    set_b = set(b)
    
    # Find symmetric difference
    sym_diff = set_a.symmetric_difference(set_b)
    
    # Convert to sorted list and return
    return sorted(sym_diff)

if __name__ == '__main__':
    m = int(input())  # Read the size of set a (not actually used)
    a = list(map(int, input().split()))  # Read the elements of set a
    n = int(input())  # Read the size of set b (not actually used)
    b = list(map(int, input().split()))  # Read the elements of set b
    
    result = symmetric_difference(a, b)
    
    # Print the results, one per line
    for value in result:
        print(value)
