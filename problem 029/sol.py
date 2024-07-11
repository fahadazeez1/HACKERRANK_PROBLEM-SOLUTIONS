# Python solution file
import cmath

# Input
complex_number = complex(input().strip())

# Calculate magnitude and phase
magnitude = abs(complex_number)
phase = cmath.phase(complex_number)

# Print the results
print(f"{magnitude:.3f}")
print(f"{phase:.3f}")
