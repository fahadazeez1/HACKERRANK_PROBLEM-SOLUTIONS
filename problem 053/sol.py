# Python solution file

english_subscribers_count = int(input())
english_subscribers = set(map(int, input().split()))

french_subscribers_count = int(input())
french_subscribers = set(map(int, input().split()))
symmetric_diff = english_subscribers.symmetric_difference(french_subscribers)
print(len(symmetric_diff))
