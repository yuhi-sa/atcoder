N = int(input())
A = map(int, input().split()) 
B = map(int, input().split()) 

Min = int(min(B))
Max = int(max(A))

if Min - Max >= 0:
    print(Min-Max+1)
else:
    print(0)