import pandas as pd
import numpy as np

data = pd.read_csv("spiral_dataset.csv")
input_matrix = data[data.columns[1:3].values]

num_of_neurons_in_layer = 5
num_of_elements_in_inputs = input_matrix.shape[1]
weight_matrix = np.random.rand(num_of_neurons_in_layer, num_of_elements_in_inputs)
weight_matrix_t = np.array(weight_matrix).T

bias_matrix = np.random.rand(num_of_neurons_in_layer)

layer_output = np.dot(input_matrix, weight_matrix_t) + bias_matrix
print(layer_output)
