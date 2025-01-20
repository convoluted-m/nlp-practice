import numpy as np

##  A batch of data with three samples each containing 4 features
inputs = [[1.0, 2.0, 3.0, 2.5], [2,5,-1,2], [-1.5, 2.7, 3.3, -0.8]]

## Matrix product and transposition
# a row vector (also a matrix of size 1 by 3)
a = [1,2,3] 
b = [2,3,4]

## Matrix multiplication - rows of 1st matrix * columns of 2nd matrix
a = np.array([a])
b = np.array([b]).T # this needs transpored into a column vector for matrix multiplication

# returns a matrix
np.dot(a,b)


## 1-layer of neurons using a batch of data
# batch of sample input data (3 samples, each with 4 features)
inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0 ,-1.0 ,2.0],
          [-1.5, 2.7, 3.3, -0.8]]


# need to turn the row vectors into column vectors to perform matrix multiplication (no of rows in m1 needs to match no of columns in m2 )
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

outputs = np.dot(inputs, np.array(weights).T) + biases
print(outputs)