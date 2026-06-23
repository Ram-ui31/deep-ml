import numpy as np

def compute_group_relative_advantage(rewards: list[float]) -> list[float]:
    """
    Compute the Group Relative Advantage for GRPO (DeepSeek-R1).
    
    Args:
        rewards: List of rewards for a group of G outputs from the same prompt.
    Returns:
        List of normalized advantages.
    """
    if not rewards:
        return []

    rewards_arr = np.array(rewards, dtype=np.float64)
    mean = np.mean(rewards_arr)
    std = np.std(rewards_arr)  # Defaults to Population SD (divides by G)
    
    # If std is exactly 0 (all rewards identical), return a list of zeros
    if std == 0.0:
        return [0.0] * len(rewards)
        
    # Small epsilon for numerical stability, matching DeepSeek's math
    eps = 1e-8 
    advantages = (rewards_arr - mean) / (std + eps)
    
    return advantages.tolist()
