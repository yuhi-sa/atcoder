N, K =map(int,input().split())
p = list(map(int,input().split()))

for i in range(N):
    for n in range(N-1):
        if p[n]>p[n+1]:
            tmp = p[n]
            p[n] = p[n+1]
            p[n+1] = tmp

ans =0
for i in range(K):
    ans += p[i]

print(ans)