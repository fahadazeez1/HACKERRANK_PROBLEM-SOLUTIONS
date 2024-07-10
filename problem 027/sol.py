# Python solution file
from itertools import permutations

# Read input
input_string, k = input().split()
k = int(k)

# Generate permutations
perm = permutations(sorted(input_string), k)

# Print permutations
for p in perm:
    print(''.join(p))
