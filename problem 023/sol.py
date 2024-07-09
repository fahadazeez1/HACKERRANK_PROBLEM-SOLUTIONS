# Python solution file

import itertools

def probability_of_a(n, letters, k):
    # Step 2: Identify indices containing 'a'
    a_indices = [i for i, letter in enumerate(letters) if letter == 'a']
    
    # Step 3: Generate all possible combinations of k indices
    all_combinations = list(itertools.combinations(range(n), k))
    
    # Step 4: Count favorable outcomes
    favorable_count = sum(1 for comb in all_combinations if any(index in comb for index in a_indices))
    
    # Step 5: Calculate the probability
    total_combinations = len(all_combinations)
    probability = favorable_count / total_combinations
    
    # Step 6: Output the result
    return round(probability, 4)

if __name__ == '__main__':
    n = int(input().strip())
    letters = input().strip().split()
    k = int(input().strip())
    
    result = probability_of_a(n, letters, k)
    print(result)
