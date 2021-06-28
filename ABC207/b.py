A, B, C, D = map(int, input().split())

blue = A
red = 0

count = 0
while(True):
    if C*D - B <= 0:
        print("-1")
        break
    if blue <= red*D:
        print(count)
        break

    blue = blue + B
    red = red + C
    count+=1