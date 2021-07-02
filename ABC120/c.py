S = list(input())

count0 = S.count('0')
count1 = S.count('1')
ans = min(count0, count1)*2
print(ans)