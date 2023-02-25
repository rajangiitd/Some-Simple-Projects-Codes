import fast_factorize
from random import randint
from functools import reduce

### Sample test cases for prime_factorization
 
# Test case 1: Product of two 10-digit primes
good = True
Ten_digit_primes = [5915587277, 1500450271, 3267000013,5754853343,4093082899, 9576890767, 3628273133, 2860486313, 5463458053, 3367900313]
for i in range(len(Ten_digit_primes)):
    for j in range(len(Ten_digit_primes)):
        P = Ten_digit_primes[i] * Ten_digit_primes[j]
        P1 = fast_factorize.prime_factorization(P)
        if(P1[0]*P1[1]!=P):
            print("Error",i,j,P,P1)
            good = False
        #else:
        #    print("OK 10-digits*10-digits",i,j,P,P1)
if(good== True):
    print("Testcase 1 OK")
            
# Test case 2: One 20-digit prime
good = True
Twenty_digit_primes = [ 48112959837082048697, 54673257461630679457,29497513910652490397, 40206835204840513073, 12764787846358441471, 71755440315342536873, 45095080578985454453, 27542476619900900873, 66405897020462343733, 36413321723440003717 ]
for i in range(len(Twenty_digit_primes)):
    P = Twenty_digit_primes[i]
    P1 = fast_factorize.prime_factorization(P)
    if( P1[0]!=P):
        print("Error",i,P,P1)
        good = False
    #else:
    #    print("OK 20 digit-prime",i,P,P1)
if(good== True):
    print("Testcase 2 OK")

# Test case 3: Product of one 20-digit prime and one 10-digit prime
good = True
for i in range(len(Twenty_digit_primes)):
    for j in range(len(Ten_digit_primes)):
        P = Twenty_digit_primes[i] * Ten_digit_primes[j]
        P1 = fast_factorize.prime_factorization(P)
        if(P1[0]*P1[1]!=P):
            print("Error",i,j,P,P1)
            good = False
        #else:
        #    print("OK 20-digits*10-digits",i,j,P,P1)
if(good== True):
    print("Testcase 3 OK")

# Test case 4: Products of first 30 primes
good = True
First_30_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
for i in range(100000):
    k = randint(1,30)   # Number of factors in the product
    P = []
    for i in range(k):
        P.append(First_30_primes[randint(0,29)])
    prime = reduce((lambda x, y: x * y), P)
    P1 = fast_factorize.prime_factorization(prime)
    if(prime != reduce((lambda x, y: x * y), P1) ):
        print("Error",i,P,P1)
        good = False
    #else:
    #    print("OK",i,P,P1)
if(good== True):
    print("Testcase 4 OK")
