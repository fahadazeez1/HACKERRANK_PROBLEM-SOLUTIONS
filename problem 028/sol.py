# Python solution file 
from collections import Counter

# Read input
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

customer_requests = []
for _ in range(num_customers):
    size, price = map(int, input().split())
    customer_requests.append((size, price))

# Initialize shoe inventory
inventory = Counter(shoe_sizes)
total_earnings = 0

# Process each customer request
for size, price in customer_requests:
    if inventory[size] > 0:
        # Sell the shoe
        total_earnings += price
        inventory[size] -= 1

# Print the earnings
print(total_earnings)
