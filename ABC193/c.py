import math
N = int(input())
num = []

for i in range(2,math.ceil(math.sqrt(N))+1):
    tmp = 1
    for n in range(2,N):
        tmp = pow(i,n)
        if tmp <= N:
            num.append(tmp)
        else:
            break

ans = N - len(set(num))
print(ans)