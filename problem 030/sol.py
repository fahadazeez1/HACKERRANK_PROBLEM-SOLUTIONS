# Python solution file
def minion_game(string):
    # Define vowels
    vowels = 'AEIOU'
    
    # Initialize scores
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    # Calculate scores
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    
    # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)