if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  # Convert map object to list

    # Find the maximum score
    max_score = max(arr)

    # Remove all occurrences of the maximum score
    arr = [score for score in arr if score != max_score]

    # Find the new maximum score which will be the runner-up
    runner_up_score = max(arr)

    # Print the runner-up score
    print(runner_up_score)
