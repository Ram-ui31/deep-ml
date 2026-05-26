import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    vals,counts=np.unique(data,return_counts=True)
    mode=vals[np.argmax(counts)]
    v=np.nanvar(data)
    a=np.percentile(data,25)
    b=np.percentile(data,75)
    c=b-a
    d={
        "mean":np.nanmean(data),
        "median":np.nanmedian(data),
        "mode":mode,
        "variance":v,
        "standard_deviation":v**0.5,
        "25th_percentile":a,
        "50th_percentile":np.percentile(data,50),
        "75th_percentile":b,
        "interquartile_range":c
    }
    return d
    pass