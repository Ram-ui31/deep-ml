import numpy as np

def compare_policy_evaluation(V: np.ndarray, P: np.ndarray, R: np.ndarray, gamma: float, n_sweeps: int, method: str) -> np.ndarray:
    """
    Perform policy evaluation sweeps using the specified update method.
    
    Args:
        V: np.ndarray of shape (n_states,), initial value function
        P: np.ndarray of shape (n_states, n_states), transition probability matrix under the policy
        R: np.ndarray of shape (n_states,), expected immediate reward for each state
        gamma: float, discount factor
        n_sweeps: int, number of sweeps to perform
        method: str, either 'synchronous' or 'in_place'
    
    Returns:
        np.ndarray: updated value function after n_sweeps
    """
    n_states=len(V)
    V1=V.copy()
    if(method=='in_place'):
        while(n_sweeps>0):
            n_sweeps-=1
            for i in range(n_states):
                sum=0
                for j in range(n_states):
                    sum+=P[i][j]*V1[j]
                V1[i]=R[i]+gamma*sum
        return V1
    else:
        while(n_sweeps>0):
            n_sweeps-=1
            for i in range(n_states):
                sum=0
                for j in range(n_states):
                    sum+=P[i][j]*V1[j]
            for i in range(n_states):
                V1[i]=R[i]+gamma*sum
        return V1
    pass