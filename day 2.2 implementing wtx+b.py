import numpy as np

inputs = [[1,     2,   3, 2.5],
          [2,     5,  -1,   2],
          [-1.5,2.7, 3.3,-0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 5]

# think it as implementing (W^T)*x + b

weight_T = np.array(weights).T

layer_output = np.dot(inputs, weight_T) + biases

print(layer_output)
