N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

count =0
a_count=0
b_count=0
ans=0 

while count<=K:
    if a_count == N and b_count == M:
        ans+=1
        break
    elif a_count == N:
        count += B[0]
        B.remove(B[0])
        b_count+=1
        ans +=1       
    elif b_count == M:
        count += A[0]
        A.remove(A[0])
        a_count+=1
        ans +=1    
    elif A[0] < B[0]:
        count += A[0]
        A.remove(A[0])
        a_count+=1
        ans +=1
    elif B[0] <= A[0]:
        count += B[0]
        B.remove(B[0])
        b_count+=1
        ans +=1
print(ans-1)