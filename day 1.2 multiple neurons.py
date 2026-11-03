inputs = [1,2,3,4]

# multiple nerons in a single layer
weights_1 = [0.1, -0.2, 0.3, -0.4]
weights_2 = [0.5, -1.0, 1.5, -2.0]
weights_3 = [0.2, -0.4, 0.6, -0.8]

bias_1 = 3
bias_2 = 2
bias_3 = 1

output = [
    inputs[0]*weights_1[0] +
    inputs[1]*weights_1[1] +
    inputs[2]*weights_1[2] +
    inputs[3]*weights_1[3] + bias_1,
    
    inputs[0]*weights_2[0] +
    inputs[1]*weights_2[1] +
    inputs[2]*weights_2[2] +
    inputs[3]*weights_2[3] + bias_2,
    
    inputs[0]*weights_3[0] +
    inputs[1]*weights_3[1] +
    inputs[2]*weights_3[2] +
    inputs[3]*weights_3[3] + bias_3
    ]

print(output)
