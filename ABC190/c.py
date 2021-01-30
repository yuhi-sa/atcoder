N,M = map(int,input().split())
# 判定条件
A = []
B = []
# 入れる方法
C = []
D = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
K = int(input())
for i in range(K):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)
##############################################################
# 答え
ans = 0
# bit全探索
bit = 0
for i in range(pow(2,K)):
    # 数えるようの受け皿
    bitF = list(format(bit,'0'+str(K)+'b'))
    # print(bitF)
    Sara = [0]*N
    # 皿に入れる
    for n in range(K):
        if bitF[n] == "0":
            Sara[C[n]-1] +=1
        elif bitF[n] == "1":
            Sara[D[n]-1] +=1
    # 判定
    # print(Sara)
    tmp = 0
    for m in range(M):
        if Sara[A[m]-1] >0 and Sara[B[m]-1]>0:
            tmp+=1
    # 回答更新
    if tmp >= ans:
        ans = tmp

    bit += 1 

print(ans)