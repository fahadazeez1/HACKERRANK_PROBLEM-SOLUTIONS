# Python solution file
def count_total_subscribers():
    # Read input
    n = int(input().strip())
    english_subscribers = set(map(int, input().strip().split()))
    m = int(input().strip())
    french_subscribers = set(map(int, input().strip().split()))
    
    # Calculate total unique subscribers
    total_subscribers = len(english_subscribers.union(french_subscribers))
    
    # Print the result
    print(total_subscribers)

# Example usage
count_total_subscribers()
