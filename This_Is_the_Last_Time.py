t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    sorted_matrix = sorted(grid, key=lambda x: (x[0], x[1], x[2]))


    for i in range(len(sorted_matrix)):
        if sorted_matrix[i][0] <= k <= sorted_matrix[i][1]:
            if k < sorted_matrix[i][2]:
                k = sorted_matrix[i][2]
                
    print(k)
