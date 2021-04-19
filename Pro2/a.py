X, Y, Z = map(int, input().split())

ans = Y*Z // X
if ans >= Y*Z /X:
    ans = ans -1
else:
    pass

if ans < 0:
    ans = 0

print(ans)