import math
S = list(input())

maru = 0
batu = 0
hate = 0

def comb(N,M):
    if N < M:
        return 0
    else:
        ans = math.factorial(N)/(math.factorial(M)*math.factorial(N-M))
        return ans

for s in S:
    if s == "o":
        maru += 1
    elif s == "x":
        batu += 1
    elif s == "?":
        hate += 1

if maru > 4 or batu == 10:
    print("0")
elif maru == 4:
    print("24")
elif maru == 3 :
    print(36 + 24*hate)
elif maru == 2:
    print(8 + 12*hate + 24*comb(hate,2))
elif maru == 1:
    print(1 + 4*hate + 12*comb(hate,2) + 24*comb(hate,3))
elif maru == 0:
    print(1*hate + 4*comb(hate,2) + 12*comb(hate,3) + 24*comb(hate,4))