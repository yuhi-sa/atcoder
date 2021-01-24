N = int(input())
L = list(map(int,input().split()))

count =0


for i in range(0, N-1):
    for n in range(0,N-1):
        if(L[n]>L[n+1]):
            tmp = L[n]
            L[n] = L[n+1]
            L[n+1] = tmp            

for i in range(0,N):
    for n in range(0,N):
        for l in range(0,N):
            if i < n and n<l:
                if L[i] != L[n]:
                    if L[n] != L[l]:
                        if L[i] != L[l]:
                            if L[i]+L[n]> L[l]:
                                count +=1

print(count)

