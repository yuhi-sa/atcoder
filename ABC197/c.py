import itertools
import math
N = int(input())
A = list(map(int,input().split()))

#######################################################

def binBin(num1,num2):
    binNum1 = list(bin(num1))
    binNum1.pop(0)
    binNum1.pop(0)
    binNum2 = list(bin(num2))
    binNum2.pop(0)
    binNum2.pop(0)

    while(len(binNum1) != len(binNum2)):
        if len(binNum1) < len(binNum2):
            binNum1.insert(0,0) 
        elif len(binNum2) < len(binNum1):
            binNum1.insert(0,0) 
    return binNum1, binNum2

def binNum(binNum):
    Num = 0
    for i in range(len(binNum)):

        if int(binNum[len(binNum)-i-1]) == 1:
            Num += pow(2,i)
    return Num 

def orCal(num1,num2):
    binNum1, binNum2 = binBin(num1,num2)
    # orの計算
    orValue = []
    for i in range(len(binNum1)):
        if int(binNum1[i]) == 1 or int(binNum2[i]) == 1:
            orValue.append(1)
        else:
            orValue.append(0)
    return binNum(orValue)

def xorCal(num1,num2):
    binNum1, binNum2 = binBin(num1,num2)
    # xor の計算
    xorValue = []
    for i in range(len(binNum1)):
        if int(binNum1[i]) == int(binNum2[i]):
            xorValue.append(0)
        else:
            xorValue.append(1)

    return binNum(xorValue)
    
#######################################################
ans = math.inf

for i in range(1,len(A)):
    a = A[0:i]
    b = A[i:len(A)]

    val1 = 0
    if len(a) == 1:
        val1 = a[0]
    else:
        val1 = orCal(a[0],a[1])
        if len(a) > 2: 
            for i in range(2,len(a)):
                val1 == orCal(val1,a[i])
    
    val2 = 0
    if len(b) == 1:
        val2 = b[0]
    else:
        val2 = orCal(b[0],b[1])
        if len(b) > 2: 
            for i in range(2,len(b)):
                val2 == orCal(val2,b[i])
    tmpAns = xorCal(val1,val2)

    if tmpAns < ans:
        ans = tmpAns

print(ans)