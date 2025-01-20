import numpy as np

# array is an ordered, honologous container for numbers
# vector is a 1-dimensional array
# matrix is a rectangular array with M rows and N columns
list_matrix = [[4,2],
               [5,1],
               [8,2]]

# A single neuron with NumPy

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights, inputs) + bias
print(outputs)

# A layer of neurons with NumPy
inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)