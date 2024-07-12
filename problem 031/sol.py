def average(array):
    unique_heights = set(array)
    
    # Calculate the average
    avg_height = sum(unique_heights) / len(unique_heights)
    
    # Return the result rounded to 3 decimal places
    return round(avg_height, 3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)# Python solution file
