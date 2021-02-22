N,K = map(int,input().split())

def solve(N):
    # １文字ずつになおす
    num = str(N)
    list_num = list(num)
    # 昇順
    up = sorted(list_num)
    # 降順
    down = list(reversed(up))
    # 文字列に戻す
    ans = int(''.join(down)) - int(''.join(up))
    return ans

ans = N
for i in range(K):
    ans = solve(ans)
print(ans)