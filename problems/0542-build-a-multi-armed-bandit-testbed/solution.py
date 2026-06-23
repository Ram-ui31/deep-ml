import numpy as np

def create_bandit_testbed(k: int, num_pulls: int, seed: int = 42) -> tuple:
    """
    Build a k-armed bandit testbed and simulate pulling each arm.
    
    Args:
        k: Number of arms
        num_pulls: Number of times to pull each arm
        seed: Random seed for reproducibility
    
    Returns:
        Tuple of (true_values, sample_means, optimal_arm)
    """
    np.random.seed(seed)
    true_values=[np.random.normal(0, 1) for _ in range(k)]
    a=true_values.index(max(true_values))
    sample_means=[0]*k
    count=0
    while(count<num_pulls):
        count+=1
        for i in range(k):
            sample_means[i]=(sample_means[i]+(np.random.normal(true_values[i],1)-sample_means[i])*(1/count))
    true_values_rounded = [round(x, 4) for x in true_values]
    sample_means_rounded = [round(x, 4) for x in sample_means]
    return (true_values_rounded,sample_means_rounded,a)
    pass