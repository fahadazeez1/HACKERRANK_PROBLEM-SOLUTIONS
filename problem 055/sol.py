# Python solution file
def avg(*args):
    return round(sum(args) / len(args), 2)

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    # Convert input to a list of integers
    args = list(map(int, input_data.split()))
    # Calculate the average
    result = avg(*args)
    # Print the result formatted to 2 decimal places
    print("{:.2f}".format(result))
