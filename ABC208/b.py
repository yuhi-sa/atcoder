import math
P = int(input())
count = 0
for i in reversed(range(1,11)):
    coin = math.factorial(i)
    if P // coin > 0 and P // coin <= 100:
        count = count + (P // coin)
        P = P%coin
    elif P // coin >= 100:
        count = count + 100
        P = P - count*100

print(count)