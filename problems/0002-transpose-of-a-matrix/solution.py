def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    # 1. Get dimensions of the original matrix
    rows = len(a)
    cols = len(a[0])
    
    # 2. Correctly initialize 'b' with the flipped dimensions (cols x rows)
    b: list[list[int|float]] = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # 3. Loop and swap elements (without the trailing colon)
    for i in range(cols):
        for j in range(rows):
            b[i][j] = a[j][i]
            
    return b  # Return the finished matrix
