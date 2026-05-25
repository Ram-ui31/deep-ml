def apply_weight_decay(parameters: list[list[float]], gradients: list[list[float]], 
                       lr: float, weight_decay: float, apply_to_all: list[bool]) -> list[list[float]]:
	"""
	Apply weight decay (L2 regularization) to parameters.
	
	Args:
		parameters: List of parameter arrays
		gradients: List of gradient arrays
		lr: Learning rate
		weight_decay: Weight decay factor
		apply_to_all: Boolean list indicating which parameter groups get weight decay
	
	Returns:
		Updated parameters
	"""
	# Your code here
	c=len(parameters[0])
	r=len(parameters)
	#updated_parameters=[[0 for j in range(c)] for i in range(r)]
	for i in range(r):
		for j in range(c):
			parameters[i][j]=parameters[i][j]-lr*gradients[i][j]-parameters[i][j]*weight_decay*lr
	return parameters
	pass