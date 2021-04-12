import math

R, X, Y = map(int,input().split())

Len = math.sqrt(X*X + Y*Y)

if Len%R == 0:
    print(int(Len/R))
elif Len < R:
    print("2")
else:
    print(int(Len//R+1))