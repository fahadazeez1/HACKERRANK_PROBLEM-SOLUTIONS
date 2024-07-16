# Python solution file
# Read the input string
input_string = input().strip()

# Initialize variables
result = []
current_char = input_string[0]
count = 1

# Iterate through the input string starting from the second character
for char in input_string[1:]:
    if char == current_char:
        count += 1
    else:
        result.append((count, current_char))
        current_char = char
        count = 1

# Append the last group
result.append((count, current_char))

# Prepare the output format
output = ' '.join(f"({count}, {char})" for count, char in result)

# Print the result
print(output)
