import math
N = int(input())
ans = math.inf
zero = 0
for i in range(N):
    A, P, X = map(int,input().split())
    if X-math.floor(A+0.5) > 0 and P < ans:
        ans = P
        zero = 1

if zero == 0:
    print(-1)
else:
    print(ans)
