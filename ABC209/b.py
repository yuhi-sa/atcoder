N , X = map(int, input().split())
A = list(map(int, input().split()))

sum = sum(A) - N//2

if sum <= X:
    print("Yes")
else:
    print("No")