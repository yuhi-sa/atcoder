N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(l[1:])
 
ans = -1
for i in range((1<<N)):
    u = [0] * M
    p = 0 #料金カウンター
    for j in range(N):
        if i & (1 << j):
            p += C[j] #料金加算
            for k in range(M):
                u[k] += A[j][k]
    if min(u) >= X: #最小値が超えたら記録
        if ans == -1 or ans > p:
            ans = p
print(ans)