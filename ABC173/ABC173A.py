N = int(input())

syo = N//1000

if N%1000 == 0:
    print(0)
else:
    amari = (syo+1)*1000 - N
    print(amari)