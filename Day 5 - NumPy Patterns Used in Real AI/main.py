import numpy as np

a = np.array([1,2,3])

# Broadcasting allows us to perform operations on arrays of different shapes and sizes. In this case, we can add
print(a + 10)

print(a.shape)

# 2D array
b = np.array([
    [1,2,3],
    [4,5,6]
])
print(b)
print(b.shape)

# Access specific elements
print(b[0, 1])  # Access the element in the first row and second
print(b[1])  # Access the second row


# Matrix multiplication =  Multiple dot products

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(np.dot(A,B))

# Transpose of a matrix
print(A.T)





