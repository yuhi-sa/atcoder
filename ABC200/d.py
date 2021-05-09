import itertools
N = int(input())
A = list(map(int, input().split()))

Stock = []
for i in range(200):
    Stock.append([])

Number = []
for i in range(1,N+1):
    Number.append(i)

for i in range(2,N+1):
    List = itertools.combinations(Number,i)
    for list in List:
        # 合計値を計算
        sum = 0
        for n in list:
            sum += A[n-1]
        Stock[sum%200].append(list)
Yes = 0
for stock in Stock:
    if len(stock) >=2:
        print("Yes")
        print(*stock[0])
        print(*stock[1])
        Yes = 1
        break

if Yes == 0:
    print("No") 