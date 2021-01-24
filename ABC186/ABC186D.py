import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
# for i in range(N):
#     for n in range(i, len(A)):
#             ans += abs(A[i]-A[n])
for pair in itertools.combinations(A, 2):
    b = list(pair)
    ans += abs(b[0]-b[1])
print(ans)
