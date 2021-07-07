import math

L ,R = map(int, input().split())

min = math.inf
for i in range(L,R+1):
    for n in range(i+1, R+1):
        tmp = (i*n)%2019
        if min > tmp:
            min = tmp
        if min == 0:
            break
    if min == 0:
        break

print(min)