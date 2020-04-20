def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    if a < b:
        return gcd(a, r)
    else:
        return gcd(b, a)

print(gcd(588, 264))