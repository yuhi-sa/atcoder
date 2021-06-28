import math
N, K = map(int, input().split())
H = []
for _ in range(N):
    h = int(input())
    H.append(h)

H.sort()
ans = math.inf

for i in range(0,N-K+1):
    diff = H[i+K-1]-H[i]
    if diff < ans:
        ans = diff

print(ans)