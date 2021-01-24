N = int(input())
D = []

ans =0
key =0
for _ in range(N):
    N,M=(map(int, input().split()))
    if N==M:
        ans +=1
    else:
        ans =0
    if ans >=3:
        key =1

if key > 0:
    print("Yes")
else:
    print("No")
