N,S,D = map(int,input().split())
ans = 0
for i in range(N):
    x,y = map(int,input().split())
    if x < S and y >D:
        ans = 1

if ans == 1:
    print("Yes")
else:
    print("No")

