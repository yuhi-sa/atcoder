a,b,c,d = map(int,input().split())

ans = b*d

if ans<a*c:
    ans = a*c

if ans<a*d:
    ans = a*d

if ans<b*c:
    ans = b*c

print(ans)