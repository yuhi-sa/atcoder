N, K = map(int,input().split())
a = list(map(int,input().split()))

# 並べ替え
a.sort()

# 最大の要素
max_value = a[len(a)-1]

# 各番号が何個あるか
box = [0] * (max_value+1)
for i in range(N):
    box[a[i]]+=1

# K個未満になるか，それ以前の最小値より小さくなれば，少なくなった個数*その値を足し算する．
ans = 0
min_num = K

for i in range(len(box)):
    if box[i] < min_num:
        ans += i*(min_num-box[i])
        min_num = box[i]
    if i == (len(box)-1) and min_num is not 0:
        ans += min_num * (i+1)
    # print("aの数",i,"合計", ans,"min_num",min_num)
print(ans)