N = int(input())
A = list(map(int,input().split()))

maxOrange = 0

for l in range(N):
    x = A[l]
    if maxOrange > x*(N-l+1):
        pass
    else:
        for r in range(l,N):
            if maxOrange > x*(N-r+1):
                break
            if A[r] < x:
                x = A[r]
            if x*(r-l+1) > maxOrange:
                maxOrange = x*(r-l+1)
        
    # print("l:",l,"r:",r,"x:",x,"max",maxOrange)

print(maxOrange)