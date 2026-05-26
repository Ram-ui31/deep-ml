import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	r=len(features)
	c=len(features[0])
	probabilities=[]
	mse=0
	for i in range(r):
		a=sum(features[i][j]*weights[j] for j in range(c))+bias
		s=1/(1+math.e**(-a))
		probabilities.append(s)
		if(labels[i]==0):
			mse+=s**2
		else:
			mse+=(1-s)**2
	mse/=r
	return probabilities, mse