import math
A, B, H, M = map(int, input().split())

A_rad = (360/12)*H + ((360/12)/60)*M
B_rad = (360/60)*M

if A_rad > B_rad:
    rad_dif = A_rad -B_rad
else:
    rad_dif = B_rad

if rad_dif > 180:
    rad_dif = 360 - rad_dif


ans = math.sqrt(A*A + B*B -2*A*B*math.cos(math.radians(rad_dif)))

print('%20.20Lf' %ans)