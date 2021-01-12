S = list(input())
T = list(input())

count =0
for i in range(len(S)):
    if S[i] != T[i]:
        count+=1

print(count)