N = int(input())
C = list(map(int, input().split()))

ans = C[0]
for i in range(1,N):
    ans = ans*(C[i]-C[i-1])

print(ans)