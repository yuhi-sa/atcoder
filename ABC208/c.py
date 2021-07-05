N , K = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append([A[i], i])
B.sort()
B = B[0:K%N]

C = [0 for i in range(N)]
for i in range(len(B)):
    C[B[i][1]]+=1

base = K // N

for i in range(N):
    if C[i] == 1:
        print(base+1)
    else:
        print(base)