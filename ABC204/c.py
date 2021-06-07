from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
  a, b = map(int, input().split())
  G[a-1].append(b-1)


ans = 0

for i in range(N):
    que = deque()
    d = [0] * N

    # 始点を訪れる
    que.append(i)
    d[i] = 1
    while len(que) > 0:
        v = que.popleft()
        for n in G[v]:
            if d[n] == 0: # 訪れたことがなかった場合
                que.append(n)
                d[n] = 1
    ans += sum(d)


print(ans)