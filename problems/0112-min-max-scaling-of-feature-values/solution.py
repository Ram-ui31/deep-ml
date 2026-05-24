def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    a=min(x)
    b=max(x)
    c=b-a
    for i in range(len(x)):
        x[i]=(x[i]-a)/c
    return x
    pass