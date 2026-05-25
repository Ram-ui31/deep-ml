import numpy as np

def detect_outliers_iqr(data: list[float], k: float) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here
	cleaned_data=[]
	outlier_indices=[]
	a=np.percentile(data,25)
	b=np.percentile(data,75)
	c=b-a
	lower_bound=a-k*c
	upper_bound=b+k*c
	for i in range(len(data)):
		if(data[i]>=lower_bound and data[i]<=upper_bound):
			cleaned_data.append(data[i])
		else:
			outlier_indices.append(i)
	dicty={
		"cleaned_data":cleaned_data,
		"outlier_indices":outlier_indices,
		"lower_bound":lower_bound,
		"upper_bound":upper_bound
	}
	return dicty
	pass