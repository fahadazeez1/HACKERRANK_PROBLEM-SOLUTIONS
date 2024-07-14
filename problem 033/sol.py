# Python solution file
def count_distinct_country_stamps():
    # Read the number of stamps
    n = int(input())
    
    # Initialize an empty set to store unique country stamps
    country_stamps = set()
    
    # Read each country name and add to the set
    for _ in range(n):
        country = input().strip()
        country_stamps.add(country)
    
    # Output the number of distinct country stamps
    print(len(country_stamps))

if __name__ == '__main__':
    count_distinct_country_stamps()
