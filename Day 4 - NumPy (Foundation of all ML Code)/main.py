import numpy as np
print(np.__version__)

a = np.array([1, 2, 3])
print(a)
print(type(a))

# Vector Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

# Vector Subtraction
print(a - b)    

# Vector Multiplication
print(a * b)

# Dot Product
print(np.dot(a, b))


# Multiplying a vector by a scalar
print(2 * a)
# Adding a scalar to a vector
print(a + 2)
