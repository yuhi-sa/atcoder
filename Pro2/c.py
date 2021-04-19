A, B = map(int, input().split())

ans = 1

# AからBの間に固定したi(1からB+1)の倍数は何個あるか
for i in reversed(range(1, B+1)):
    if B//i - (A-1)//i >= 2:
        ans = i
        break

print(ans)
