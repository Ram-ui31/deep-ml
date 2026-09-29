import numpy as np

def simple_self_attention(X: list[list[float]]) -> list[list[float]]:
    """
    Compute context vectors using simple self-attention (no trainable weights).

    Args:
        X: Input embeddings of shape (T, d) as a list of lists.

    Returns:
        Context vectors of shape (T, d) as a list of lists.
    """
	X=np.array(X)
	Y=X@(X.T)
	Y=np.exp(Y)
	A=np.sum(Y,axis=1,keepdims=True)
	Y=Y/A
	return (Y@X).tolist()
    pass
