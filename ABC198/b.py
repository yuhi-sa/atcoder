N = list(input())

ans = 1
# 回文チェック
for i in range(len(N)//2):
    if N[i] != N[len(N)-1-i]:
        ans = 0
        break

if ans == 1:
    print("Yes")

else:
    # 0カウンター
    num = 0
    for n in reversed(range(len(N))):
        if N[n] == '0':
            num+=1
        else:
            break
    # 0を足して調べる
    for n in range(num):
        ans = 1
        N = ['0']+ N
        # 回文チェック
        for i in range(len(N)//2):
            if N[i] != N[len(N)-1-i]:
                ans = 0
                break
        if ans == 1:
            print("Yes")
            break

if ans == 0:
    print("No")