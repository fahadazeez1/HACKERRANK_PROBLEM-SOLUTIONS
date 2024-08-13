# Python solution file
t = int(input())

for _ in range(t):
    # Size of set A
    a_size = int(input())
    # Elements of set A
    a = set(map(int, input().split()))
    
    # Size of set B
    b_size = int(input())
    # Elements of set B
    b = set(map(int, input().split()))
    
    # Check if A is a subset of B
    print(a.issubset(b))
