A, B, C, D = map(int, input().split())

ans = 0

if A == B+C+D:
    ans =1
if B == A+C+D:
    ans =1
if C == A+B+D:
    ans =1
if D == A+B+C:
    ans =1

if A+B == C+D:
    ans =1
if A+C == B+D:
    ans =1
if A+D == B+C:
    ans =1
    

if ans==1:
    print("Yes")
else:
    print("No")