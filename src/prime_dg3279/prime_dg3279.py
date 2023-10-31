import math

def is_prime(n):
    """
    Detects if a number is prime or not.
    
    Parameters
    ----------
    n: An integer
    
    Returns
    -------
    A True or False Bool value
    
    Examples
    --------
    >>> from prime_dg3279 import is_prime
    >>> is_prime(3)
    True
    >>> is_prime(6)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True