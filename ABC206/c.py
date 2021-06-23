import math

N = int(input())
A = list(map(int, input().split()))

A.sort()
B = [0]
C = [0]

for i in range(len(A)):
    if A[i] == B[-1]:
        C[-1]+= 1
    else:
        B.append(A[i])
        C.append(1)

diff = 0

for i in range(1,len(C)):
    if C[i] == 1:
        pass
    else:
        diff += math.factorial(C[i])/(2*math.factorial(C[i]-2))

sum = N*(N-1)//2

print(int(sum - diff))