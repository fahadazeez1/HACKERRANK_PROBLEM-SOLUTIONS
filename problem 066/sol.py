# Solution file
import re

def find_valid_hex_colors(n, lines):
    hex_pattern = re.compile(r'#(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6})\b')
    valid_colors = []
    
    
    for line in lines:
        # Ignore lines that are selectors
        if ':' in line:
            # Find all matches in the current line
            matches = hex_pattern.findall(line)
            # Add matches to the valid colors list
            valid_colors.extend(matches)
    
   
    for color in valid_colors:
        print(color)

n = int(input().strip())
lines = [input().strip() for _ in range(n)]
find_valid_hex_colors(n, lines)
