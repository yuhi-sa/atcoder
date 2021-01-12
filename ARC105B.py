N = int(input())
a = list(map(int,input().split()))
a.sort()
Max = a[-1]
Min = a[0]

for _ in range(N*N):

    if a[-2]+Min < a[-1]:
        a[-1] = a[-1] - ((a[-2]-a[-1])%Min)*Min
        Max = a[-1]
    else:
        #最大値更新
        for i  in reversed(range(len(a))):
            if a[0] >= Max-Min:
                a.insert(0,Max-Min)
                break
            if a[i] <= Max-Min:
                a.insert(i+1,Max-Min)
                break

        #最小値更新
        Min = a[0]
        
        #現在の最大値を取得
        Max = a.pop(-1)

    if Max == Min:
        break


print(Max)