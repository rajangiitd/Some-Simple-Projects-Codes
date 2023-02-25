import numpy as np
mod = (10**9) +7
def fib_sum_upto(x):
    if(x<=2):
        return max(0,x)
    x=x-1
    arr=np.ones((3,3), dtype = int)
    arr[0][0],arr[0][2],arr[1][2]=0,0,0
    ans = np.eye(3,dtype= int)
    while(x>0):
        if(x&1):
            ans = np.matmul(ans,arr)%mod
        arr= np.matmul(arr,arr)%mod
        x=(x>>1)
    return ans[2][1]+ans[2][2]
'''  returns (F[0]+F[1]+F[2]+..........+F[x]) % mod

Used matrix exponentiation as follows to calculate the sum of fibonacci numbers upto x
[ Fn-1    ]   = [0,1,0]^(n-1) [0= F0]
[ Fn      ]   = [1,1,0]       [1= F1]
[ SigmaFn ]   = [1,1,1]       [1= SigmaF1]
'''