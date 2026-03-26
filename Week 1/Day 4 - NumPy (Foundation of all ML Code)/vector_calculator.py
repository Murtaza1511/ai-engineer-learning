import numpy as np

def vector_calculator(a, b):
    a = np.array(a)
    b = np.array(b)
    
    print("A + B =", a + b)
    print("A - B =", a - b)
    print("A * B (element-wise) =", a * b)
    print("Dot Product =", np.dot(a, b))

# Test
vector_calculator([1,2,3], [4,5,6])