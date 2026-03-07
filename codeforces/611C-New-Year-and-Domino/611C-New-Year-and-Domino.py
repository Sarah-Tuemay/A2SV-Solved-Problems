# prefix sum
horizontal_pre = [[0]*(w+1 )for i in range(h+1)]
vertiacal_pre = [[0]*(w+1) for j in range(h+1)]
for i in range(1,h+1):
    for j in range(1,w+1):
        horizontal_pre[i][j] = horizontal_pre[i-1][j] + horizontal_pre[i][j-1] - horizontal_pre[i-1][j-1] + horizontal[i-1][j-1]  
        vertiacal_pre[i][j] = vertiacal_pre[i-1][j] + vertiacal_pre[i][j-1] - vertiacal_pre[i-1][j-1] + vertiacal[i-1][j-1]
q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    horizontal_count = (
        horizontal_pre[r2][c2-1]
        - horizontal_pre[r1-1][c2-1]
        - horizontal_pre[r2][c1-1]
        + horizontal_pre[r1-1][c1-1]
    )

    vertiacal_count = (vertiacal_pre[r2-1][c2] - vertiacal_pre[r1-1][c2]-vertiacal_pre[r2-1][c1-1] + vertiacal_pre[r1-1][c1-1])

    print(horizontal_count+vertiacal_count)