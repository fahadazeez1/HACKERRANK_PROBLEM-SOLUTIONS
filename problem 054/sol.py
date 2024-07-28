# Python solution file
if __name__ == '__main__':
    # Reading the first line to get n and m
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    # Reading the next n lines to get the rows of the table
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Reading the last line to get k
    k = int(input().strip())

    # Sorting the array based on the k-th attribute
    sorted_arr = sorted(arr, key=lambda x: x[k])

    # Printing the sorted array
    for row in sorted_arr:
        print(" ".join(map(str, row)))
