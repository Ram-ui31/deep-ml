def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	rows=len(matrix)
	columns=len(matrix[0])
	for r in range(rows):
		for c in range(columns):
			matrix[r][c]*=scalar
	return matrix
	pass