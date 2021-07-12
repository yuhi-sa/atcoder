A , B = map(int, input().split())

ans = B-A+1
if ans <= 0:
    print(0)
else:
    print(ans)