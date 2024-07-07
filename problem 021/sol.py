if __name__ == '__main__':
    string = input().strip()
    
    # Check for any alphanumeric characters
    has_alnum = any(char.isalnum() for char in string)
    print(has_alnum)
    
    # Check for any alphabetical characters
    has_alpha = any(char.isalpha() for char in string)
    print(has_alpha)
    
    # Check for any digits
    has_digit = any(char.isdigit() for char in string)
    print(has_digit)
    
    # Check for any lowercase characters
    has_lower = any(char.islower() for char in string)
    print(has_lower)
    
    # Check for any uppercase characters
    has_upper = any(char.isupper() for char in string)
    print(has_upper)
# Python solution file
