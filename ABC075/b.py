H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

MAP = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for n in range(W):
        if S[i][n] == "#":
            # 上
            if i != 0:
                MAP[i-1][n] += 1
                # 上左
                if n != 0:
                    MAP[i-1][n-1] += 1
                # 上右
                if n != W-1:
                    MAP[i-1][n+1] += 1

            # 左
            if n != 0:
                    MAP[i][n-1] += 1
            # 右
            if n != W-1:
                MAP[i][n+1] += 1

            # 下
            if i != H-1:
                MAP[i+1][n] += 1
                # 下左
                if n != 0:
                    MAP[i+1][n-1] += 1
                # 下右
                if n != W-1:
                    MAP[i+1][n+1] += 1
            
for i in range(H):
    for n in range(W):
        if S[i][n] == "#":
            MAP[i][n] = "#" 
        else:
            MAP[i][n] = str(MAP[i][n])

    print("".join(MAP[i]))

