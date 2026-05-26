import math

def sigmoid(z: float) -> float:
	#Your code here
	a=1+math.e**(-z)
	result=1/a
	return result