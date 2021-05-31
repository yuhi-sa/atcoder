N, K = map(int, input().split())
Data = []
for _ in range(N):
    Data.append(list(map(int, input().split())))

# A, Bの並び替え
Data.sort()

pos = 0

for i in range(N):
    # print("所持金:",K, "現在位置:",pos, "次の目的位置:",Data[i][0])
    
    # A_iにたどりつける場合
    if pos + K >= Data[i][0]:
        K = K - (Data[i][0]-pos) + Data[i][1]
        pos = Data[i][0]
        
    # A_iにたどり着けない場合
    else:
        pos = pos + K
        break

    # 一番最後
    if i == N-1:
        pos = pos + K

print(pos)