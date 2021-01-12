H,W = map(int, input().split())
A = []

min = 101

for i in range(H):
    A.append(list(map(int, input().split())))
    for n in range(W):
        if min > A[i][n]:
            min = A[i][n]

ans = 0

for i in range(H):
    for n in range(W):
        ans += A[i][n]-min
    
print(ans)