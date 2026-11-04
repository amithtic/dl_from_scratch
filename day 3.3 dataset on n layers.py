import pandas as pd
import numpy as np

data = pd.read_csv("spiral_dataset.csv")
input_matrix = data[data.columns[1:3].values]

no_of_neurons = [2,3,4,5,3,2,1]

for i in range(len(no_of_neurons)):
    num_of_neurons_in_layer = no_of_neurons[i]
    num_of_elements_in_inputs = input_matrix.shape[1]
    weight_matrix = np.random.rand(num_of_neurons_in_layer,
                                   num_of_elements_in_inputs)
    weight_matrix_t = np.array(weight_matrix).T
    bias_matrix = np.random.rand(num_of_neurons_in_layer)
    layer_output = np.dot(input_matrix, weight_matrix_t) + bias_matrix
    input_matrix = layer_output
    
print(layer_output)
