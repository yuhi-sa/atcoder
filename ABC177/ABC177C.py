N = int(input())
A = list(map(int,input().split()))

ans =0
sum = sum(A)
for i in range(N-1):
    sum-=A[i]
    ans+=A[i]*sum

ans = ans % 1000000007
print(ans)