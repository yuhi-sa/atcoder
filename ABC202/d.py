import itertools
A, B , K = map(int, input().split())
N = A+B

def maxNumber(N):
    ans = 0
    for i in range(N):
        ans += pow(2,i)
    return ans

# 2進数変換
def binbinmake(N):
    ans = []
    maxNum = maxNumber(N)
    for i in range(maxNum+1):
        # 2進数変換
        tmp = list(bin(i))
        # 0bを消す
        tmp.pop(0)
        tmp.pop(0)
        # N文字にする
        while(len(tmp) < N):
            tmp = ["0"] + tmp
        ans.append(tmp)

    return ans

def makeans(boxLen):
    ans = ""
    for i in range(len(boxLen)):
        if boxLen[i]== 0:
            ans += "a"
        else:
            ans += "b"

    return ans



Box = itertools.product([0,1], repeat=N)
count = 0

for box in Box:
    a_num = box.count(0)
    b_num = box.count(1)
    if a_num <= A and b_num <= B:
        count += 1
    if count == K:
        ans = makeans(box)
        print(ans)
        break