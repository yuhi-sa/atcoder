import numpy as np
a = input().split()
H = int(a[0])
W = int(a[1])
K = int(a[2])

C=np.zeros((H,W),dtype=str)
for i in range(H):
    C[i,:]= np.array(list(input()))

count =0

for S in range(2**(H+W)-1):
    p = np.zeros(H+W)
    s = np.append(p,np.array(list(bin(S))))

    ans = 0
    for i in range(H):
        for n in range(W):
            if  s[-n]== '0' or s[-n]== 'b':
               continue
            if  s[-(W+i)] == '0' or s[-(W+i)] == 'b':
               continue
            if C[i,n]=='#':
                ans+=1
    if ans == K:
        count+=1

print(count)
            