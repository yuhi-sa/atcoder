A, B, C, X, Y = map(int, input().split())

# ABで揃えられる最小枚数
mixAB = min(X, Y)

# 最小のABで揃えた場合の費用
costABmin = mixAB*2*C + (X-mixAB)*A + (Y-mixAB)*B

# ABで揃えられる最大枚数
maxAB = max(X, Y)
# 最大のABで揃えた場合の費用
costABmax = maxAB*2*C 

# 別々で揃えた場合の費用
cost = X*A + Y*B

tmp = min(costABmax, costABmin)
ans = min(tmp, cost)

print(ans)