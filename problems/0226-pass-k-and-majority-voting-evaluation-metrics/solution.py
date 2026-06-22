import numpy as np
from collections import Counter
import math

def pass_at_1(responses_correct: np.ndarray) -> float:
	"""
	Compute pass@1 by averaging correctness.
	
	Args:
		responses_correct: Boolean array for each response
		
	Returns:
		pass@1 score
	"""
	# Your code here
	a=0
	for el in responses_correct:
		if(el==True):
			a+=1
	return a/len(responses_correct)
	pass


def majority_voting(responses: list[str]) -> str:
	"""
	Return the most common response.
	
	Args:
		responses: List of response strings
		
	Returns:
		Most frequent response
	"""
	# Your code here
	return Counter(responses).most_common(1)[0][0]
	pass


def pass_at_k(n: int, c: int, k: int) -> float:
	"""
	Compute unbiased pass@k from n samples with c correct.
	
	Formula: pass@k = 1 - C(n-c, k) / C(n, k)
	
	Args:
		n: Total samples
		c: Correct samples
		k: k in pass@k
		
	Returns:
		Estimated pass@k
	"""
	# Your code here
	return 1-math.comb(n-c,k)/math.comb(n,k)
	pass