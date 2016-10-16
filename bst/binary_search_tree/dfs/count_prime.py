# count prime number up to N
from math import sqrt

def isPrime(n):
    # check for 1, 2
    if n <= 2:
        return False
    # check for even numbers
    if n % 2 == 0:
        return False
    result = True
    # only count to upto sqrt(n)
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            result = False
    return result


print isPrime(999)