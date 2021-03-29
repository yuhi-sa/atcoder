import math
N = int(input())
A = []
B = []

minA = math.inf
minB = math.inf

for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    if a <= minA:
        minA = a
        numA = i
    if b <= minB:
        minB = b
        numB = i

count = 0

secondMinA = math.inf
secondMinB = math.inf

for i in range(N):
    if A[i] == minA:
        count+=1
    if B[i] == minB:
        count +=1
    if A[i] <= secondMinA and A[i] is not minA:
        secondMinA = A[i]
    if B[i] <= secondMinB and B[i] is not minB:
        secondMinB = B[i]

an1 = max(minA,secondMinB)
an2 = max(secondMinA, minB)
an3 = minA + minB

if numA is not numB:
    print(max(minA,minB))
elif count >= 3:
    print(max(minA,minB))
else:
    tmp = min(an2,an3)
    print(min(an1,tmp))
