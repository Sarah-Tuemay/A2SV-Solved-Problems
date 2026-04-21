class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0),(1, 0), (0,-1),(0,1)]

        def is_edge(row, col):
            return row == 0 or col == 0 or row == rows-1 or col == cols-1
        
        def not_valid(row, col):
            return row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] == 'X' or board[row][col] == '1'

        def dfs(row, col):
            # print(row, col, not_valid(row, col))
            if not_valid(row, col):
                return
            
            board[row][col] = '1'

            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                dfs(new_row, new_col)
            



        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and is_edge(i, j):
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '1': board[i][j] = 'O'
        # print(board)
