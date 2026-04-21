class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(-1,0),(0,-1),(0,1),(1,0)]
        rows = len(grid)
        cols = len(grid[0])
        ans = [0]

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(-1, 0),(1, 0), (0,-1),(0,1)]

        def not_valid(row, col):
            return(row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0')

        def dfs(row, col, grid):

            if not_valid(row, col):
                return
            
            grid[row][col] = '0'

            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc 
                dfs(new_row, new_col,grid)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans[0] += 1

                    dfs(i, j, grid)
        
        return ans[0]


        