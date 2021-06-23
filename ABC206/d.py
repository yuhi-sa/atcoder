N = int(input())
A = list(map(int, input().split()))

left = []
right = []
for i in range(N//2):
    if A[i]!= A[N-1-i]:
        left.append(A[i])
        right.append(A[N-1-i])

diff = 0
miss = 0
for i in left:
    if i in right:
        diff += 1
    else:
        miss += 1

for i in right:
    if i in left:
        pass
    else:
        miss += 1


if diff == 0 and miss == 0:
    print(0)
else:
    print(diff -  1 + miss)