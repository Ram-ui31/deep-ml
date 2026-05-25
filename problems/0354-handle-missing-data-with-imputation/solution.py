import numpy as np


def impute_missing_data(data: np.ndarray, strategy: str) -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    c=len(data[0])
    r=len(data)
    if(strategy=='mean'):
        for i in range(c):
            column_data=data[:,i]
            column_data[np.isnan(column_data)]=np.nanmean(column_data)
            data[:,i]=column_data
    elif(strategy=='median'):
        for i in range(c):
            column_data=data[:,i]
            column_data[np.isnan(column_data)]=np.nanmedian(column_data)
            data[:,i]=column_data
    elif strategy == 'mode':
        for i in range(c):
            column_data = data[:, i]
        
        # 1. Extract only the valid, non-NaN values from the column
            clean_values = column_data[~np.isnan(column_data)]
        
        # 2. Handle edge case: if the column has NO valid numbers (all NaNs)
            if len(clean_values) == 0:
                mode_val = 0.0  # Fallback baseline
            else:
            # 3. Count frequencies of unique values
                vals, counts = np.unique(clean_values, return_counts=True)
            
            # 4. Use argmax to find the value with the highest frequency count
                mode_val = vals[np.argmax(counts)]
            
        # 5. Overwrite the NaNs in the original array column view
            column_data[np.isnan(column_data)] = mode_val
            data[:,i]=column_data
    return data
    pass