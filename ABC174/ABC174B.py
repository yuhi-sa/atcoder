s = input().split()
N = int(s[0])
D = int(s[1])

count =0
for i in range(0,N):
    a,b = input().split()
    a = int(a)
    b = int(b)
    length = a*a+b*b
    if length <=D*D:
        count+=1

print(count)