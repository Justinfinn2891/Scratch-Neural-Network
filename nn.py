import numpy as np

#small example of input layer
input = [3,4,2, 2.5]

weights1 = [0,3,3, 1]
weights2 = [0,3,3, 1]
weights3 = [0,3,3, 1]

bias1 = 3
bias2 = 3
bias3 = 3



#single neuron from the network with three inputs 
#every input has its own unique weight but every neuron has one bias 
output = [input[0]*weight1[0] + input[1]*weight1[1] + input[2]*weight1[2] weight1[2] + input[3]*weight1[3] + bias1],
[input[0]*weight2[0] + input[1]*weight2[1] + input[2]*weight2[2] weight2[2] + input[3]*weight2[3] + bias2],
[input[0]*weight3[0] + input[1]*weight3[1] + input[2]*weight3[2] weight3[2] + input[3]*weights3[3] + bias3]


print(output)

#Simplifying the code

weights = [[0,3,3, 1], [0,3,3, 1], [0,3,3, 1]]
biases = [2, 3, .5]

some_value = .05
weight = .06
bias = .7 

#Numpy work 

output = np.dot((weights, inputs) + bias)

#Dot product, look at shaping issue 

