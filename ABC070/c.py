X = abs(int(input()))

count = 1
sum = 0
while(True):
    sum = sum + count
    if sum >=X:
        break
    else:
        count = count + 1

print(count)
