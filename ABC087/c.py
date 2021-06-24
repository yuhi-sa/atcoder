N = int(input())
A = []
for i in range(2):
    A.append(list(map(int,input().split())))

ans = 0
for i in range(N):
    tmp = sum(A[0][0:i+1]) +sum(A[1][i:N])
    if tmp > ans:
        ans = tmp
print(ans)