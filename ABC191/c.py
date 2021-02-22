H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))

black = 0

for i in range(H):
    for n in range(W):
        if S[i][n] == "#":
            continue
        # 1行目を確認
        if i is 0:
            #端の場合
            if n is 0 or n is W-1:
                black+=1
            #中央の場合
            


print(black)