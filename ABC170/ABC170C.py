import numpy as np
X,N = map(int,input().split())

if N ==0:
    print(X)

else:
    p = list(map(int,input().split()))

    length =np.zeros(102)
    length =list(length)

    for i in range(len(length)):
        length[i]= abs(X-i)

    for i in range(N):
        length[p[i]]=1000

    ans = length.index(min(length))
    print(ans)
