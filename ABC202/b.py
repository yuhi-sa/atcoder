S = list(input())
ans = []

for i in range(len(S)):
    if S[i] == "0":
        ans.append("0")
    elif S[i] == "1":
        ans.append("1")
    elif S[i] == "6":
        ans.append("9")
    elif S[i] == "8":
        ans.append("8")
    elif S[i] == "9":
        ans.append("6")

ansans = ""
for i in reversed(range(len(S))):
    ansans += ans[i]

print(ansans)