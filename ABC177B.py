S = input()
T = input()

if len(S)==len(T):
    count=0
    for i in range(len(T)):
        if T[i] != S[i]:
            count+=1
    print(count)

else:
    countbox=[]
    for n in range(len(S)-len(T)+1):
        count =0
        for i in range(len(T)):
            if T[i] != S[i+n]:
                count+=1
        countbox.append(count)
    print(min(countbox))