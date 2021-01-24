N = int(input())
S = []
for i in range(N):
    S.append(str(input()))

S.sort()
ans = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        ans += 1

print(ans)



# A = []
# for i in range(N):
#     ans = 1
#     if len(A)>0:
#         for n in range(len(A)):
#             if str(A[n]) == str(S[i]):
#                 ans = 0
    
#     if len(A) == 0:
#         A.append(S[i])

#     elif ans == 1:
#         A.append(S[i])

# print(len(A))