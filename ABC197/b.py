H, W, X, Y = map(int,input().split())
MAS = []
for _ in range(H):
    MAS.append(list(input()))

#######################################
# 配列番号を整える
X = X - 1
Y = Y - 1

## 探索
ans = 0

# 自分自身
if MAS[X][Y] == ".":
    ans += 1

# 縦列マイナス
i = X
while(True):
    if i == X:
        pass
    elif i < 0:
        break
    elif MAS[i][Y] == "#":
        break
    elif MAS[i][Y] == ".":
        ans += 1
    i -= 1

# 縦列プラス
i = X
while(True):
    if i == X:
        pass
    elif i > H-1:
        break
    elif MAS[i][Y] == "#":
        break
    elif MAS[i][Y] == ".":
        ans += 1
    i += 1

# 横列マイナス
n = Y
while(True):
    if n == Y:
        pass
    elif n < 0:
        break
    elif MAS[X][n] == "#":
        break
    elif MAS[X][n] == ".":
        ans += 1
    n -= 1

# 横列プラス
n = Y
while(True):
    if n == Y:
        pass
    elif n > W-1:
        break
    elif MAS[X][n] == "#":
        break
    elif MAS[X][n] == ".":
        ans += 1
    n += 1

print(ans)