l = list(input())

ans = 0
for i in range(len(l)):
    # 偶数
    if (i+1)%2==0:
        # 大文字
        if l[i].isupper():
            pass
        #　小文字
        else:
            ans = 1
    else:
        if l[i].isupper():
            ans = 1
        else:
            pass
    
if ans == 0:
    print("Yes")
else:
    print("No")
    