K = int(input())
s = list(input())
t = list(input())

# K枚以上出ないかチェック
check = [K,K,K,K,K,K,K,K,K]

# 初期化
S = []
for i in range(4):
    S.append(int(s[i]))
    check[S[-1]-1] -= 1
T = []
for i in range(4):
    T.append(int(t[i]))
    check[T[-1]-1] -= 1

# 合計値の計算
def cal(num):
    box = [0,0,0,0,0,0,0,0,0]
    for i in range(5):
        box[num[i]-1]+=1
    ans = 0
    for i in range(1,10):
        if box[i-1]==0:
            ans += i
        else:
            ans += i*pow(10,box[i-1])
    return ans

ans = 0
pattern = 0
# 組み合わせ確認
for i in range(1,9):
    if check[i-1] == 0:
        pass
    else:
        check[i-1] -= 1
        tmpS = S
        tmpS.append(i)
        for n in range(1,9):
            if check[n-1] == 0:
                pass
            else:
                check[n-1] -= 1
                tmpT = T
                tmpT.append(n)
                if cal(tmpS) > cal(tmpT):
                    print(i,n)
                    ans += 1/(check[i-1]+1)*(check[n-1]+1)
                check[n-1] += 1
        check[i-1] += 1
print(ans)
    
        
