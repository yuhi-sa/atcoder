import math
# N = int(input())
N = 12

# 差1の等差数列の和aは初項,nは項数
def sumsum(a,n):
    return int(n*(2*a+n-1)/2)

# 解の個数
def ansans(a,N):
    tmp = 0
    val1 = -(2*a-1)+ math.sqrt((2*a-1)*(2*a-1)+8*N)
    val2 = -(2*a-1)+ math.sqrt((2*a-1)*(2*a-1)+8*N)
    if val1.is_integer() and val1 >=0:
        tmp+=1
    if val2.is_integer() and val1 >=0:
        tmp+=1
    return tmp



# 答え
ans = 0

for a in range(N+1):
    ans += sumsum(a,N)

print(ans*2)

