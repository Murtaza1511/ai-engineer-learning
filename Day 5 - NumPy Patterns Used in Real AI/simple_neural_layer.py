
import numpy as np

def neural_layer(x, W, b):
    x = np.array(x)
    W = np.array(W)
    b = np.array(b)
    
    return np.dot(W, x) + b

# Test
output = neural_layer(
    [1,2],
    [[3,4],[5,6]],
    [1,1]
)

print("Output:", output)