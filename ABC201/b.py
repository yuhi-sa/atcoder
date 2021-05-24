N = int(input())
S = []
T = []
sortList = []
for _ in range(N):
    s, t = map(str, input().split())
    t = int(t)
    S.append(s)
    T.append(t)
    sortList.append(t)

sortList.sort()

# print(S)
# print(T)
# print(sortList)
for i in range(N):
    if sortList[N-2] == T[i]:
        print(S[i])