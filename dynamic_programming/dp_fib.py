# Dynamic programming on fibonacci
class dpFib(object):
    def __init__(self):
        self.result = {0: 0, 1: 1}

    def fib(self, n):
        # top down approach
        if n in self.result:
            return self.result[n]
        self.result[n] = self.fib(n-1) + self.fib(n-2)
        return self.result[n]

    def fib_bottom_up(self, n):
        result = [0, 1]
        for i in xrange(2, n+1):
            result.append(result[i-1] + result[i-2])
        return result[n]

def memoize(f):
    cache = {}

    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    memoizedFunction.cache = cache
    return memoizedFunction

@memoize
def fib_memo(n):
    if n <= 2:
        return 1
    else:
        return fib_memo(n-1) + fib_memo(n-2)



#test = dpFib()
#print test.fib(8)

#import timeit
#print timeit.Timer('test.fib(900)', 'from __main__ import dpFib; test=dpFib(); gc.enable()').timeit(10)