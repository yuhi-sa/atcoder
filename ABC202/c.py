N = int(input())
MAP = []
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Field = [0 for _ in range(N+1)]

for i in range(N):
    # Aの要素
    Field[int(A[i])] += 1

Field2 = [0 for _ in range(N+1)]
for n in C:
    # CのindexのBの要素
    Field2[int(B[n-1])] += 1

ans = 0
for i in range(N+1):
    ans += Field[i]*Field2[i]

print(ans)