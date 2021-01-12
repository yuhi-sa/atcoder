L = list(map(int,input().split()))
A = L[0]
K = L[1]
D = L[2]

if A/D>K:
    ans = A - D*K
else:
    e = A//D-1
    K -= e
    A =e*D
    if K%2 == 1:
        K=abs(K-D)
    ans = K

print(ans)