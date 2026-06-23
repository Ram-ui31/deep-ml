def sample_average_action_values(k: int, actions: list, rewards: list) -> tuple:
    """
    Estimate action values using sample averaging.
    
    Args:
        k: Number of possible actions (labeled 0 to k-1)
        actions: List of actions taken at each time step
        rewards: List of rewards received at each time step
        
    Returns:
        Tuple of (Q, N) where Q is estimated values and N is selection counts
    """
    t=len(actions)
    N=[0]*k
    S=[0.0]*k
    for i in range(t):
        N[actions[i]]+=1
        S[actions[i]]+=rewards[i]
    for i in range(k):
        if(N[i]!=0):
            S[i]/=N[i]
    Q=[round(x,4) for x in S]
    N1=[round(x,4) for x in N]
    return (Q,N1)
    pass