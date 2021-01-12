N, S = input().split()

A_count = 0
T_count = 0
C_count = 0
G_count = 0

kaburi = 0

for i in range(len(S)):
    if S[i] == 'A':
        A_count+=1
    elif S[i] == 'T':
        T_count+=1
    elif S[i] == 'C':
        C_count+=1
    elif S[i] == 'G':
        G_count+=1
    if i != len(S)-1:
         if S[i]=='A' and S[i+1]=='T':
             kaburi +=1
         elif S[i]=='T' and S[i+1]=='A':
             kaburi +=1
         elif S[i]=='C' and S[i+1]=='G':
             kaburi +=1
         elif S[i]=='G' and S[i+1]=='C':
             kaburi +=1

ans = - kaburi

if A_count <= T_count:
    ans += A_count*2
elif A_count > T_count:
    ans += T_count*2

if C_count <= G_count:
    ans += C_count*2
elif C_count > G_count:
    ans += G_count*2

print(ans)