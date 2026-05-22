def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows=len(matrix)
	columns=len(matrix[0])
	
	if(mode=='column'):
		means : list[float] = []
		for c in range(columns):
			sum=0
			for r in range(rows):
				sum+=matrix[r][c]
			means.append(sum/rows)
	else:
		means : list[float] = []
		for r in range(rows):
			sum=0
			for c in range(columns):
				sum+=matrix[r][c]
			means.append(sum/columns)			
	return means