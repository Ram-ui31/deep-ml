import numpy as np
import math
def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	b=np.zeros(len(scores))
	s=0
	m=max(scores)
	for i in scores:
		s+=math.e**(i-m)
	for i in range(len(scores)):
		b[i]=scores[i]-m-math.log(s)
	return b
	pass