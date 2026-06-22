import numpy as np

def epsilon_greedy(Q, epsilon=0.1):
    """
    Selects an action using epsilon-greedy policy.
    Q: np.ndarray of shape (n,) -- estimated action values
    epsilon: float in [0, 1]
    Returns: int, selected action index
    """
    n = len(Q)

    if np.random.rand() < epsilon:
        # 2. Use np.random.choice(n) to choose the random exploration action
        return np.random.choice(n)
    else:
        # 3. Exploit the greedy action
        return np.argmax(Q)

