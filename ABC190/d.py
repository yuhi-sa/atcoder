# N = int(input())
n = 1

def check(n,ans,l):
    tmp = abs(n*n/l-l+1)
    if tmp%2 == 0:
        ans+=1
    return ans

ans = 0
x = 0
while(x*x<=n*n):
    x += 1
    if n*n%x == 0:
        y = int(n*n/x)
        ans = check(n,ans,x)
        if y!= x:
            ans = check(n,ans,y)
    print(x,y,ans)

print(ans)