# 1, iteration
# 2, recursion
# 3, dynamic programming

class factorial(object):

    def __init__(self):
        self.result = {0: 1}

    def fac_iter(self, n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def fac_dp(self, n):
        # save the intermediate result to self.result
        if n in self.result:
            print 'return: n is ', n
            return self.result[n]
        print 'fac_dp(', n, ')'
        r = self.fac_dp(n-1) * n
        self.result[n] = r
        return r

    def fac_re(self, n):
        # base case
        if n == 1:
            return 1
        return self.fac_re(n-1) * n

if __name__ == "__main__":
    f = factorial()
    print f.fac_re(10)
    print f.fac_iter(10)