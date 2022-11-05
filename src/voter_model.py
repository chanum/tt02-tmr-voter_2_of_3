
def voter_model(a: int, b: int, c: int):
    """Model of voter 2 of 3"""
    r = 0
    e = 1

    # calc output
    if a == b:
        r = a
    elif a == c:
        r = a
    else:
        r = b

    # calc error
    if a == b and b == c:
        e = 0

    return r, e
