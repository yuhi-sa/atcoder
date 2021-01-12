N = int(input())

ans = 0
for i in range(N):
    n = i+1
    if  "7" not in str(n) and "7" not in str(format(n, 'o')):
        ans += 1

print(ans)