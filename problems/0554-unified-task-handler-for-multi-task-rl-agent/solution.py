import numpy as np

def unified_task_handler(state_features: np.ndarray, task_weights: np.ndarray, task_id: int, epsilon: float = 0.0) -> dict:
    """
    Compute task-conditioned action values and epsilon-greedy action probabilities.

    Args:
        state_features: (num_actions, feature_dim) feature vectors for each action
        task_weights: (num_tasks, feature_dim) weight vectors for each task
        task_id: integer index of the current task
        epsilon: exploration parameter for epsilon-greedy (0 <= epsilon <= 1)

    Returns:
        dict with keys:
          - 'q_values': numpy array of shape (num_actions,)
          - 'greedy_action': int
          - 'action_probs': numpy array of shape (num_actions,)
    """
    k=state_features.shape[0]
    c=state_features.shape[1]
    q_values=np.zeros(k)
    for i in range(k):
        for j in range(c):
            q_values[i]+=state_features[i][j]*task_weights[task_id][j]
    dic={}
    dic['q_values']=q_values
    dic['greedy_action']=np.argmax(q_values)
    action_probs=[(epsilon-epsilon/k)/(k-1)]*k
    action_probs[np.argmax(q_values)]=1-epsilon+epsilon/k
    dic['action_probs']=action_probs
    return dic
    pass