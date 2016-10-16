# fibonacci series
import numpy as np
# fn = fn-1 + fn-2
# 1 ,1, 2, 3, 5, 8 ,13, 21

# recursive
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

# loop
def fib_loop(n):
    if n < 3:
        return 1
    prev = 1
    current = 1
    result = 1
    for i in xrange(3, n+1):
        result = prev + current
        prev = current
        current = result
    return result

# quick fibonacci
# O(logn) instead of O(n)
# find matrix, A, s.t., [f(n+1), f(n)] = A^n * [f(1) f(0)]

def fib_fast(n):
    A = np.matrix([[1,1],[1,0]])
    power = matrix_helper(A, n)
    r = power * np.matrix('1;0')
    return r[1,0]

def matrix_helper(M, n):
    # compute power of a matrix
    # return numpy.matrix
    if n == 1:
        return M
    r1 = matrix_helper(M, n/2)
    r = r1 * r1
    if n % 2 != 0:
        # if odd number
        r *= M
    return r

if __name__ == "_main__":
    print fib(8)
    print fib_loop(8)
    print fib_fast(8)
