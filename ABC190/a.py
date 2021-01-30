A,B,C = map(int,input().split())

while(1):
    if C == 0:
        if A <= 0:
            print("Aoki")
            break
        A -=1
        C = 1
    elif C == 1:
        if B <= 0:
            print("Takahashi")
            break
        B -=1
        C = 0

