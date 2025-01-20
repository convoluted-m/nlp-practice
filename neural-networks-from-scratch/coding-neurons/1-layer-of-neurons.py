### 1-layer network 
 
## With a single neuron
# One sample with 4 features (sample/observation = feature set)
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = (inputs[0]*weights[0]+
          inputs[1]*weights[1]+
          inputs[2]*weights[2]+
          inputs[3]*weights[3] + bias)
print(output)

## 1 layer of 3 neurons
inputs = [1,2,3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0]*weights1[0]+
          inputs[1]*weights1[1]+
          inputs[2]*weights1[2]+
          inputs[3]*weights1[3] + bias1,
  
          inputs[0]*weights2[0]+
          inputs[1]*weights2[1]+
          inputs[2]*weights2[2]+
          inputs[3]*weights2[3] + bias2,

          inputs[0]*weights3[0]+
          inputs[1]*weights3[1]+
          inputs[2]*weights3[2]+
          inputs[3]*weights3[3] + bias3]

print(output)

## 1 layer of  3 neurons with a for loop
inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

layer_outputs = []

# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        # ultiply input by weight and add to neuron's output
        neuron_output += n_input * weight
    # add bias
    neuron_output +=neuron_bias
    # append to the layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)