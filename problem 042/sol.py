# Python solution file
# Read input values
n = int(input())
english_subs = set(map(int, input().split()))

m = int(input())
french_subs = set(map(int, input().split()))

# Find the intersection of the two sets
both_subs = english_subs.intersection(french_subs)

# Output the number of students in the intersection
print(len(both_subs))
