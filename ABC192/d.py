N = int(input())
M = int(input())

# 最大値dを求める
num = str(N)
list_num = list(num)
up = sorted(list_num)
d = up[len(up)-1]

# 10進数→N進法
def change(N,shinsu):
    keta=0
    for i in range(10**9):
        if N<shinsu**i:
             keta+=i
             break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//(shinsu**(keta-i))
        ans[check]=str(j)
        check+=1
        N-=(j)*(shinsu**(keta-i))
    return int(''.join(ans))

# N進法→10進数
def henkan(N,shinsu):
    num = str(N)
    list_num = list(num)
    ans=0
    for i in range(1,len(list_num)+1):
        ans+=int(list_num[-i])*(shinsu**(i-1))
    return ans

ans = 0
change = 0
i = int(d)+1

while(change <= M):
    if i in list(str(N)):
        break
    elif i < 36:
        change =  int(str(N), i)
        i+=1
        ans+=1
    else:
        change =  henkan(N,i)
        i+=1
        ans+=1

print(ans-1)