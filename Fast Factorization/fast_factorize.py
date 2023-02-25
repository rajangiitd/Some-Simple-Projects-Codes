from collections import defaultdict
import math

#### It uses deterministic Miller Rabin, pollard algorithm with brent cycle etc.

def binpower(base, e, mod):
    res = 1
    base %= mod
    while (e > 0):
        if (e & 1):
            res = (res * base) % mod
        e = e>>1
        base = (base * base) % mod
    return res

def check_composite(n,a,d,s):
    x= binpower(a,d,n)
    if(x==1 or x== n-1):
        return False
    for r in range(1,s):
        x= (x*x)%n
        if(x== n-1):
            return False
    return True

def MillerRabin(n):
    ### return true if n is prime , works for n= 1 to 1e18
    if(n<2):
        return False
    r=0
    d= n-1
    while((d&1)==0):
        d= (d>>1)
        r+=1

    L= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for a in L:
        if(n==a):
            return True
        if(check_composite(n,a,d,r)):
            return False
    return True

def mult(a,b,mod):
    return (a*b)%mod

def f(x,c,mod):
    return ((x*x) + c)%mod

def rho(n,x0=2,c=1):
    x= x0
    y= x0
    g= 1
    while(g==1):
        x=f(x,c,n)
        y=f(y,c,n)
        y=f(y,c,n)
        g= math.gcd(abs(x-y),n)
    return g

def brent(n,x0=2,c=1):
    x= x0
    g=1
    q=1
    xs,y=-1,-1
    m= 128
    l=1
    while(g==1):
        y=x
        for i in range(l):
            x= f(x,c,n)
        k=0
        while(k<l and g==1):
            xs= x
            for i in range(min(m,l-k)):
                x = f(x,c,n)
                q = mult(q,abs(y-x),n)
            g = math.gcd(q,n)
            k+=m
        l= l*2
    if(g==n):
        attempt=1
        while(attempt==1 or g==1):
            xs= f(xs,c,n)
            g= math.gcd(abs(xs-y),n)
            attempt=2
    return g

def count_divisors(n):
    #### returns count of all positive divisors of n
    fac=[]
    if(n<=2):
        return n
    if(MillerRabin(n)):
        return 2
    
    fac=[]
    for i in range(2,100):
        while(n%i==0):
            fac.append(i)
            n= n//i
    while(MillerRabin(n)==False and n>1):
        f= brent(n)
        tryy=30
        while(MillerRabin(f)==False and tryy>0):
            tryy-=1
            f= brent(f)
        if(f==1):
            continue
        while(n%f==0):
            fac.append(f)
            n= n//f
    if(n>1):
        fac.append(n)
    freq = defaultdict(int)
    ans=1
    for item in fac:
        freq[item]+=1
    for item in freq:
        ans = ans * (freq[item]+1 )
    return ans

def prime_factorization(n):
    #### returns list of prime_factorization for n>=2
    fac=[]
    if(n<=1):
        print("Invalid Input")
        return [-1]
    if(MillerRabin(n)):
        return [n]
    fac=[]
    for i in range(2,100):
        while(n%i==0):
            fac.append(i)
            n= n//i
    while(MillerRabin(n)==False and n>1):
        f= brent(n)
        tryy=30
        while(MillerRabin(f)==False and tryy>0):
            tryy-=1
            f= brent(f)
        if(f==1):
            continue
        while(n%f==0):
            fac.append(f)
            n= n//f
    if(n>1):
        fac.append(n)
    return fac