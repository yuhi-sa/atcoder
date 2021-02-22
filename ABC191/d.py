import math
X,Y,R = map(float, input().split())

high = math.floor(Y + R) # 小数点以下切り捨て
low = math.ceil(Y - R) # 小数点以下を切り上げ

X = X*100000
Y = Y*100000
R = R*100000
high = high*100000
low = low*100000

# x軸上にある格子点を求める
def sol(y,r):
    x_right = (X+math.sqrt(r*r-y*y))/100000
    x_left = (X-math.sqrt(r*r-y*y))/100000
    return math.floor(x_right) - math.ceil(x_left) + 1

ans = 0
# 上から下までx軸上の格子点を求める
for i in range(low, high+100000, 100000):
    ans += sol(i-Y,R)

print(ans)