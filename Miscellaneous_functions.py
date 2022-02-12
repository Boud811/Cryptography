def gcd(a, b):
    if a > b:
        return gcd(b,a)
    if a ==0: 
        return b
    return gcd(a, b%a)

def Extendedgcd(a,b):
    """
    returns 3 numbers, gcd(a,b), x, y such that ax + by = gcd(a, b)
    """
    if a> b:
        return Extendedgcd(b,a)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = Extendedgcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y




def MultiplicativeInverse(a, n):
    """
    returns the multiplicative inverse of a mod n 
    Args: a --int-- the number you'd like to find the inverse of 
        n --int-- the modulo you're working in 
    
    """
    out = Extendedgcd(a, n)[1]
    if out<0:
        out = n+ out
    return out