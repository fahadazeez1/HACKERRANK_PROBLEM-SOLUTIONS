# Python solution file
from collections import deque

# Read the number of operations
n = int(input().strip())

# Initialize an empty deque
dq = deque()

# Process each operation
for _ in range(n):
    operation = input().strip().split()
    if operation[0] == 'append':
        dq.append(int(operation[1]))
    elif operation[0] == 'appendleft':
        dq.appendleft(int(operation[1]))
    elif operation[0] == 'pop':
        dq.pop()
    elif operation[0] == 'popleft':
        dq.popleft()

# Print the elements of the deque
print(' '.join(map(str, dq)))
