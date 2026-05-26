import numpy as np
import math
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	r=len(features)
	c=len(features[0])
	mse_values=[0]*epochs
	updated_weights=np.copy(initial_weights)
	updated_bias=initial_bias
	l=learning_rate
	for e in range(epochs):
		s=0
		dw=[0]*c
		dc=0
		w=updated_weights.T
		for i in range(r):
			a=-(features[i]@w+updated_bias)
			b=1/(1+math.e**a)
			s+=((labels[i]-b)**2)/r

			dc+=(2/r)*(b-labels[i])*b*(1-b)

			for j in range(c):
				dw[j]+=(2/r)*(b-labels[i])*b*(1-b)*features[i][j]
		for j in range(c):
			updated_weights[j]=updated_weights[j]-l*dw[j]
		updated_bias=updated_bias-l*dc
		mse_values[e]=s
	return updated_weights, updated_bias, mse_values