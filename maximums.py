def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        return x
    elif x < y:
        return y
    else: 
        return x
def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x > y and x > z:
        return x 
    elif z > x and z > y:
        return z
    else:
        return y
