N = int(input())
A = list(map(int, input().split()))

count = 1
clash = 0
for i in range(N):
    if count == A[i]:
        count += 1
    else:
        clash += 1

if count == 1:
    print(-1)
else:
    print(clash)
    