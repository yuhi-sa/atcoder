import math
N = int(input())
A = list(map(int, input().split()))

Even = []
Odd = []
Eindex = []
Oindex = []

for i in range(100):
    Even.append([])
    Odd.append([])

for a in A:
    if (a//100) % 2 == 0:
        Even[a%100].append(a//100)
        Eindex.append(a%100)
    else:
        Odd[a%100].append(a//100)
        Oindex.append(a%100)      
 
# 重複削除
Eindex = list(set(Eindex))
Oindex = list(set(Oindex))

ans = 0
for i in Eindex:
    if len(Even[i]) == 1:
        ans += 0
    elif len(Even[i]) == 2:
        ans += 1
        # print(Even[i],1)
    else:
        ans += math.factorial(len(Even[i]))/(2*math.factorial(len(Even[i])-2))
        # print(Even[i],math.factorial(len(Even[i]))/(2*math.factorial(len(Even[i])-2)))

for i in Oindex:
    if len(Odd[i]) == 1:
        ans += 0
    elif len(Odd[i]) == 2:
        ans += 1
        # print(Odd[i], 1)
    else:
        ans += math.factorial(len(Odd[i]))/(2*math.factorial(len(Odd[i])-2))
        # print(Odd[i], math.factorial(len(Odd[i]))/(2*math.factorial(len(Odd[i])-2)))

print(int(ans))