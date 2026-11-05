inputs = [1,2,3,4]
weights = [0.1, -0.2, 0.3, -0.4]
bias = 3

output = bias

for i in range(len(inputs)):
    output = output + (inputs[i] * weights[i])
    
print(output)

Edited by Amit NOde in a copied (forked) repo.
