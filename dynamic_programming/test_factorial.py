import timeit

print "Recursion"
print timeit.Timer('f.fac_re(900)', 'from factorial import factorial; f = factorial();').timeit(10)

print "Iteration"
print timeit.Timer('f.fac_iter(900)', 'from factorial import factorial; f = factorial();').timeit(10)

print "Dynamic Programming"
print timeit.Timer('f.fac_dp(5)', 'from factorial import factorial; f = factorial();').timeit(10)