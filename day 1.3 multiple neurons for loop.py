inputs = [1,2,3,4]

# multiple nerons in a single layer
weights = [[0.1, -0.2, 0.3, -0.4],
             [0.5, -1.0, 1.5, -2.0],
             [0.2, -0.4, 0.6, -0.8]]
bias = [3, 2, 1]

output = []

for i in range(len(weights)):
    x = 0
    x = x + bias[i]
    for j in range(len(inputs)):
        x = x + (inputs[j] * weights[i][j])
    output.append(x)

print(output)
