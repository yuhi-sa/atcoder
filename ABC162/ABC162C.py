K = int(input())

def gcd(p, q):
    if p % q==0:
        return q
    return gcd(p, p% q)

tmp = 0
ans = 0
for i in range(1,K+1):
    for n in range(1,K+1):
        tmp = gcd(i,n)
        for l in range(1,K+1):
            ans += gcd(tmp,l) 

print(ans)
