import math

N,K = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = math.inf
for i in range(N-K+1):
    for n in range(N-K+1):

        # 選択される池の範囲
        ike = []
        for tate in range(0,K):
            for yoko in range(0,K):
                ike.append(A[i+tate][n+yoko])

        # 中央値を計算
        ike.sort()
        median = ike[-(K*K//2+1)]
        print("池:",ike, "中央値：",median, "最小の中央値:",ans)
        if ans > median:
            ans = median
    
print(ans)