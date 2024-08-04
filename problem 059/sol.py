# Python solution file
import re

def is_valid_float(s):
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    if re.match(pattern, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    else:
        return False
n = int(input().strip())
for _ in range(n):
    s = input().strip()
    print(is_valid_float(s))
