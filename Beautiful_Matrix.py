matrix = []
for i in range(5):
    ele = list(map(int, input().split()))
    matrix.append(ele)

indices = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            indices.append(i)
            indices.append(j)
            break

ans = 0
for index in indices:
    if index != 2:
        ans += abs(index-2)
print(ans)
