# In RSA Cryptosystem, the public key consists of a pair of numbers(e, n) where
# the sender taeks the message x and raises it to the power e mod n
# n usually the product of two large primes n = p*q   
#
# And the private key consists of a pair of numbers (phi(n), d) 
# where de = 1 mod phi(n), and phi(n)=(p-1)*(q-1)
# When we recieve an enrypted message y = x^e mod n 
# we raise it to the power d mod n 
# y^d = (x^e)^d = x^ed = x mod n by Fermat's little theorem
#

import random as rnd
from Primality_tests import RepMRTest, MRTest
from Miscellaneous_functions import Extendedgcd, MultiplicativeInverse, gcd

def generate_large_probable_prime_candidates(length):
    """
    returns an odd number of the given length
    length: number of bits the candidate has
    """
    x = rnd.getrandbits(length)

    x = x | (1 << length -1 ) | 1
    return x 

def generate_large_probable_prime(length, number_of_tests = 1024):
    p=4
    while not RepMRTest(p, number_of_tests, log= False):
        p  = generate_large_probable_prime_candidates(length)
    return p

def generate_encryption_public_key(phi_n):
    e = 2
    
    while gcd(e, phi_n)!= 1: 
        e = rnd.randint(2, phi_n)
        print(e)
        
    return e 




def generate_RSA_keys(primes_length=256):
    """
    returns a tuple (n, e, d, phi(n))
    """
    p = generate_large_probable_prime(primes_length)
    q = generate_large_probable_prime(primes_length)
    phi_n = (p-1)*(q-1)
    n = p*q
    e = generate_encryption_public_key(phi_n)
    d = MultiplicativeInverse(e, phi_n)

    return n, e, d, phi_n


x = 24



def RSAEncryption(message,n, e):
    return pow(message, e, n)

def RSADecryption(CipheredMessage, n, d):
    return pow(CipheredMessage, d, n)

n, e , d, phi_n = generate_RSA_keys(256)

print("n= ",n,"\ne= ", e, "\nd= ", d, "\nphi(n)=", phi_n)
y=  RSAEncryption(x, n, e)
print('y= ',y) 
print("x= ", RSADecryption(y, n, d))
