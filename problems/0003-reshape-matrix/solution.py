import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    rows=len(a)
    columns=len(a[0])
    if (rows * columns) != (new_shape[0] * new_shape[1]):
        return []
    b = np.array(a)
    c = b.reshape(new_shape)
    reshaped_matrix = c.tolist()
    return reshaped_matrix