N, M = map(int, input().split())
A = input().split()
B = input().split()

C = []

for i in range(N):
    tmp = 0
    for n in range(M):
        if A[i] == B[n]:
            tmp = 1
            break
    if tmp == 0:
        C.append(int(A[i]))


for i in range(M):
    tmp = 0
    for n in range(N):
        if B[i] == A[n]:
            tmp = 1
            break
    if tmp == 0:
        C.append(int(B[i]))

C.sort()

print(*C)