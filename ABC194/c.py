import itertools
N = int(input())
A = input().split()

for i in range(N):
    A[i] = int(A[i])

ans = 0
for p in itertools.combinations(A, 2):
        ans += pow((p[0]-p[1]),2)

print(ans)