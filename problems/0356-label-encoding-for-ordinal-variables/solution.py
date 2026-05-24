def search(a: str,b: list) -> int:
    for i in range(len(b)):
        if(a==b[i]):
            return i
        elif(i==len(b)-1):
            return -1
    pass

def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest

    Returns:
        List of integers representing the encoded values
    """
    l=[0]*len(values)
    for i in range(len(values)):
        l[i]=search(values[i],order)
    return l
    pass