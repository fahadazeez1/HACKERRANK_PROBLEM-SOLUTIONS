# Python solution file
from itertools import product

def maximize_value(n, M, lists):
    max_modulo_sum = 0
    
    # Generate all combinations of elements from the lists
    combinations = product(*lists)
    
    # Iterate through each combination
    for combo in combinations:
        # Calculate the sum of squares modulo M for this combination
        modulo_sum = sum(num**2 for num in combo) % M
        # Update max_modulo_sum if this combination gives a higher value
        if modulo_sum > max_modulo_sum:
            max_modulo_sum = modulo_sum
    
    return max_modulo_sum

# Reading input
n, M = map(int, input().split())
lists = []
for _ in range(n):
    lists.append(list(map(int, input().split()[1:])))

# Calculate and print the result
result = maximize_value(n, M, lists)
print(result)

