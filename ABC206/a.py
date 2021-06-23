N = int(input())

if N*1.08 < 206:
    print("Yay!")
elif 207 > N*1.08 >= 206:
    print("so-so")
else:
    print(":(")