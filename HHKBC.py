N = int(input())
p = list(map(int, input().split()))

Max = max(p)
sample = {i for i in range(Max+2)}

for i in range(N):
    if p[i] in sample:
        sample.remove(p[i])
    print(min(sample))