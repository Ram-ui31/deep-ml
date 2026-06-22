import numpy as np
import math

def softmaxer(theta: np.ndarray):
    for i in range(theta.shape[0]):
        sum=0
        for j in range(theta.shape[1]):
            theta[i][j]=math.exp(theta[i][j])
            sum+=theta[i][j]
        for j in range(theta.shape[1]):
            theta[i][j]/=sum

def compute_policy_gradient(theta: np.ndarray, episodes: list[list[tuple[int, int, float]]]) -> np.ndarray:
    """
    Estimate the policy gradient using REINFORCE.

    Args:
        theta: (num_states x num_actions) policy parameters.
        episodes: List of episodes, where each episode is a list of (state, action, reward).

    Returns:
        Average policy gradient (same shape as theta).
    """
    # Your code here
    a=theta.shape[1]
    s=theta.shape[0]
    theta_grad=np.zeros((s,a))
    n_epi=len(episodes)
    softmaxer(theta)
    for i in range(n_epi):
        n_steps=len(episodes[i])
        g=0
        for j in range(n_steps):
            g+=episodes[i][j][2]
        for j in range(n_steps):
            for c in range(a):
                theta_grad[episodes[i][j][0]][c]+=g*(-theta[episodes[i][j][0]][c])
            theta_grad[episodes[i][j][0]][episodes[i][j][1]]+=g

    for el in theta_grad:
        el/=n_epi
    return theta_grad
    pass