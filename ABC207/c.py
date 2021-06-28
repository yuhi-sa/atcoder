import itertools

N = int(input())

l = [0] * 1000000000
print("配列")
for _ in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        l[l] += 1
        l[r+1] -= 1
    elif t == 2:
        l[l] += 1
        l[r] -= 1      
    elif t == 3:
        l[l+1] += 1
        l[r+1] -= 1 
    elif t == 4:
        l[l+1] += 1
        l[r] -= 1 
print("acc")
acc = list(itertools.accumulate(l))
print("acc2")
print(len(l)-acc.count(0))
