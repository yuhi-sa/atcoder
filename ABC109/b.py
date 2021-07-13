N = int(input())

def computeSum(n):
    return n*(n+1)//2

def binarySearch(N):
    first = 1
    last  = N

    limit_value = N + 1

    while(True):
        mid = (first+last)//2
        mid_value = computeSum(mid)
        
        if (last - first) == 1:
            return mid - 1 

        elif mid_value > limit_value:
            last = mid

        else:
            first = mid

if N == 1 or N == 2:
    print(1)
else:
    ans = binarySearch(N)
    print(N - ans)