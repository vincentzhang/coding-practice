# Test fib implementations
# 1, iteration
# 2, recursion
# 3, dynamic programming

import timeit

#print "Recursion"
#print timeit.Timer('fib.fib(32)', 'import fib; gc.enable()').timeit(1)
print "Iteration"
print timeit.Timer('fib.fib_loop(100)', 'import fib; gc.enable()').timeit(10)
print "Fast, matrix"
print timeit.Timer('fib.fib_fast(100)', 'import fib; gc.enable()').timeit(10)
print "Dynamic Programming , top down"
print timeit.Timer('f.fib(100)', 'from dp_fib import dpFib; f=dpFib(); gc.enable()').timeit(10)
print "Dynamic Programming , top down decorator"
print timeit.Timer('dp_fib.fib_memo(100)', 'import dp_fib; gc.enable()').timeit(10)
print "Dynamic Programming , bottom up"
print timeit.Timer('f.fib_bottom_up(100)', 'from dp_fib import dpFib; f=dpFib(); gc.enable()').timeit(10)