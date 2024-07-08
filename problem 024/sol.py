# Python solution file
from collections import OrderedDict

def count_words(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    distinct_word_count = len(word_count)
    occurrences = ' '.join(map(str, word_count.values()))
    
    print(distinct_word_count)
    print(occurrences)

if __name__ == '__main__':
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    
    count_words(n, words)