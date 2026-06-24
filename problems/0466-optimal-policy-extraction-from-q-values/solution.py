import numpy as np

def extract_optimal_policy(Q: np.ndarray) -> dict:
    """
    Extract the optimal policy, state-value function, and advantage
    function from a Q-value table.
    
    Args:
        Q: Q-value table of shape (num_states, num_actions)
    
    Returns:
        Dictionary with keys:
        - 'optimal_actions': list of int (optimal action per state)
        - 'state_values': list of float (V*(s) per state)
        - 'advantages': nested list of float (A(s,a) for all pairs)
    """
    s, a = Q.shape
    state_values=[0]*s
    optimal_actions=[0]*s
    dic2={}
    for i in range(s):
        optimal_actions[i]=np.argmax(Q[i])
        state_values[i]=Q[i][np.argmax(Q[i])]
        for j in range(a):
            Q[i][j]-=state_values[i]
    for i in range(s):
        for j in range(a):
            Q[i][j]=round(Q[i][j],4)
    dic={}
    dic['optimal_actions']=optimal_actions
    dic['state_values']=state_values
    dic['advantages']=Q.tolist()
    return dic
    pass