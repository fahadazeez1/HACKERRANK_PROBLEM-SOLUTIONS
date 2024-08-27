# Solution file 
import numpy as np

# Take input from user
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

# Compute inner product
inner_product = np.inner(A, B)

# Compute outer product
outer_product = np.outer(A, B)

# Print results
print(inner_product)
print(outer_product)



