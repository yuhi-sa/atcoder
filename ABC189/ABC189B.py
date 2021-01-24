N, X = map(int,input().split())
alc = 0
tmp = "-1"
for i in range(N):
    V,P=map(int,input().split())
    alc += V*P
    if alc > X*100 and tmp == "-1":
        tmp = i+1

print(tmp)

