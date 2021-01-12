N = int (input())

S = [input() for i in range(0,N)]

C0=0 #AC
C1=0 #WA
C2=0 #TLE
C3=0 #RE

for i in range(0,N):
    if S[i]=='AC':
        C0+=1
    elif S[i]=='WA':
        C1+=1
    elif S[i]=='TLE':
        C2+=1
    elif S[i]=='RE':
        C3+=1

print('AC x', C0)
print('WA x', C1)
print('TLE x', C2)
print('RE x', C3)