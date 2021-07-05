N ,M =map(int, input().split())

MAP = [[0 for i in range(N)]for i in range(N) ]

for i in range(M):
    a, b, c = map(int, input().split())
    MAP[a-1][b-1] = c

print(MAP)

