import numpy as np
import math

def ucb_action(counts, values, t, c):
    """
    Choose an action using the UCB1 formula.
    Args:
      counts (np.ndarray): Number of times each action has been chosen
      values (np.ndarray): Average reward of each action
      t (int): Current timestep (starts from 1)
      c (float): Exploration coefficient
    Returns:
      int: Index of action to select
    """
    # TODO: Implement the UCB action selection
    ucb_array=np.zeros(counts.shape[0])
    for i in range(values.shape[0]):
      ucb_array[i]+=values[i]+c*((math.log(t)/counts[i])**1/2)
    return np.argmax(ucb_array)
    pass