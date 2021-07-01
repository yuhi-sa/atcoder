N, M = map(int, input().split())
BOX = []
for _ in range(N):
    a, b = map(int, input().split())
    BOX.append([a,b])

BOX.sort()

count = 0
sum = 0

for i in range(N):
    if count + BOX[i][1] >= M:
        sum += BOX[i][0]*(M-count)
        break
    else:
        count = count + BOX[i][1]
        sum = sum + BOX[i][0]*BOX[i][1]

print(sum)