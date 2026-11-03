import numpy as np

inputs = [1,2,3,4]

# multiple nerons in a single layer
weights = [[0.1, -0.2, 0.3, -0.4],
             [0.5, -1.0, 1.5, -2.0],
             [0.2, -0.4, 0.6, -0.8]]
bias = [3, 2, 1]

layer_output = np.dot(weights, inputs) + bias

print(layer_output)
