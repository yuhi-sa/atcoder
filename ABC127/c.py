N, M = map(int, input().split())

left = 0
right = N

flag = True
for i in range(M):
    l,r = map(int, input().split())

    if l > left and l <= right:
	    left = l

    if r < right and r >= left:
	    right = r
    
    if r < left or l > right:
        flag = False

if flag == True:
    print(right - left + 1)
else:
    print(0)