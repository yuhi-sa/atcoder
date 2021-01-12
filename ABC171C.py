N = int(input())
ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

a = []

s = ''
while(N>0):
    N=N-1
    s+=ALPHABET[N%26]
    N = N//26

print(s)