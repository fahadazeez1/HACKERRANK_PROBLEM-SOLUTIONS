# Python solution file
 width = len(bin(number)) - 2

    
    for i in range(1, number + 1):
        # Print the formatted values 
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")
