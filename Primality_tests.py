import random as rnd

def gcd(a, b):
    if b< a:
        return gcd(b, a)
    r = b%a
    return gcd(a, r)


def FermatsTest(n, base=2, log= True):
    passing = pow(base, n-1, n) ==1 
    if log: 
        print("Fermat's test passed: ", passing, "\nFor the number: ", n,"\nIn the base: ", base)
    return passing


def MRTest(n, base =2, log =True):
    d = n - 1
    r=0 
    if n ==2 or n==3:
        return True
    if n&1==0 :
        return False
    while d&1 == 0:
        d //= 2
        r += 1
    # n = 2^(r) d + 1
    x = pow(base, d, n)
    if x !=  1:
        for i in range(1, r):
            if log:
                print("x = ", x, "\nCalculating x^2: ", pow(x, 2, n))
            x = pow(x, 2, n)
        
            if x==n-1:
                if log: 
                    print("Miller Rabin's test passed: ", True, "\nFor the number: ", n,"\nIn the base: ", base)
                return True

            elif x==1: 
                break
            
        if log:
            print("Miller Rabin's test passed: ", False, "\nFor the number: ", n,"\nIn the base: ", base, "\nFaliure at: 2^",i," * ", d )
        return False
    
    if log: 
        print("Miller Rabin's test passed: ", True, "\nFor the number: ", n,"\nIn the base: ", base)
    return True

def RepMRTest(n, k =10, log=True):
    witnesses =[]
    for _ in range(k):
        base= rnd.randint(2,n-2)
        witnesses.append(base)
        if not MRTest(n, base, log):
            if log: 
                print("Witness of compositeness: ", witnesses[-1])
            return False

    if log:        
        print("Witnesses of primeness ", witnesses)
    return True
#TODO add more tests
# while True:
#     test = input("Which test would you like to preforme?\n1- Fermat's Test. \n2- MR's Test.\n3- Repeated MR's Test.\n")
#     if test == "1":
#         n = int(input("Enter the number you'd like to test: "))
#         base = int(input("Enter the base you'd like to test on: "))

#         FermatsTest(n, base)
#         input("Press any key to continue.")
#     elif test == "2":
#         n = int(input("Enter the number you'd like to test: "))
#         base = int(input("Enter the base you'd like to test on: "))

#         MRTest(n, base)
#         input("Press any key to continue.")

#     elif test == "3":
#         n = int(input("Enter the number you'd like to test: "))
#         k = int(input("Enter the number of random bases you'd like to test on: "))

#         RepMRTest(n, k)
#         input("Press any key to continue.")

#     else:
#         input("Invalid input, Press any key to continue.")

