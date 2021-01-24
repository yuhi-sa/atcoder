a = input()

count = 0
max_count =0
for i in range(3):
    if a[i] == "S":
        count = 0
    elif a[i] == "R":
        count = count + 1
    if max_count <count:
        max_count = count

print(max_count)