N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

max = a[0]*b[0]
max_a = 0
for i in range(N):
    if max_a < a[i]:
        max_a = a[i]
    if max < max_a*b[i]:
        max = max_a*b[i]
    print(max)