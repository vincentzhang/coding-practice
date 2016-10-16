# gcd algorithm
# Recursion
# A = B*Q + R
# gcd(A,B) = gcd(B, R)
def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print gcd(270, 192)
