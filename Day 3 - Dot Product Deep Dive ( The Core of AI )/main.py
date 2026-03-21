import numpy as np

# Similar Vectors
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
print(np.dot(a, b))

# Orthogonal Vectors
c = np.array([1, 0, 0])
d = np.array([0, 1, 0])
print(np.dot(c, d))

# Opposite Vectors
e = np.array([1, 2, 3])
f = np.array([-1, -2, -3])
print(np.dot(e, f))

# Mini Project: Analyze Vector Relationships
def analyze_vectors(a, b):
    dot = np.dot(a, b)
    
    print("Vector A:", a)
    print("Vector B:", b)
    print("Dot Product:", dot)
    
    if dot > 0:
        print("→ Positively aligned")
    elif dot < 0:
        print("→ Opposite direction")
    else:
        print("→ Perpendicular / unrelated")

# Test
analyze_vectors([1,2,3], [2,4,6])
analyze_vectors([1,0], [0,1])
analyze_vectors([1,2,3], [-1,-2,-3])
