import numpy as np
np.random.seed(0)

X = [[1 , 2 , 3 , 2.5 ],
          [2.0,5.0,-1.0,2.0],
          [-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs,n_neurons) # by n_inputs divided by n_nuerons the weights will be transversed.
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)+ self.biases


layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
print(layer1.output)
print('\n\n')
layer2.forward(layer1.output)
print(layer2.output)


