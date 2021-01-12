K = int(input())
count =1

x = 7%K

for i in range(0,K+1):
    if x== 0:
        print(count)
        break

    count+=1
    x = (x*10+7)%K

if i== K:  
    print(-1)