import numpy as np

def optimistic_greedy_bandit(
    true_rewards: list,
    initial_q: float,
    n_steps: int,
    step_size: float
) -> tuple:
    """
    Simulate a greedy bandit agent with optimistic initialization.
    
    Args:
        true_rewards: List of true deterministic rewards for each arm
        initial_q: Optimistic initial Q-value for all arms
        n_steps: Number of steps to simulate
        step_size: Constant step-size (alpha) for Q-value updates
    
    Returns:
        Tuple of (Q_values, action_counts) where Q_values is a list of
        floats rounded to 4 decimal places, and action_counts is a list of ints.
    """
    # Your code here
    r=len(true_rewards)
    q_values=[initial_q]*r
    counts=[0]*r
    #q_prev+alpha*(r-q_prev)
    while(n_steps>0):
        n_steps-=1
        i=q_values.index(max(q_values))
        q_values[i]=q_values[i]+step_size*(true_rewards[i]-q_values[i])
        counts[i]+=1
    result=((q_values),(counts)) 
    return result   
    pass