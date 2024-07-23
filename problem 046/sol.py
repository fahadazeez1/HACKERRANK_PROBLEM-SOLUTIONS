# Python solution file
from collections import Counter

def find_captains_room(k, room_list):
    # Count the frequency of each room number
    room_counter = Counter(room_list)
    
    # Identify the room number that appears exactly once
    for room, count in room_counter.items():
        if count == 1:
            return room

if __name__ == "__main__":
    # Input the size of each group
    k = int(input())
    
    # Input the list of room numbers
    room_list = list(map(int, input().split()))
    
    # Find and print the Captain's room number
    captain_room = find_captains_room(k, room_list)
    print(captain_room)
