H, W = map(int, input().split())
S =[]
for i in range(H):
    S.append(list(input()))

ans = 0

for i in range(H):
    for n in range(W):
        if n == W-1:
            pass
        elif S[i][n] == S[i][n+1] and S[i][n] == '.':
            ans +=1

for n in range(W):
    for i in range(H):
        if i == H-1:
            pass
        elif S[i][n] == S[i+1][n] and S[i][n] == '.':
            ans +=1

print(ans)