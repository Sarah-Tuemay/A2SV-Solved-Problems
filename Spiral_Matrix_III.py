class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        row, col = rStart, cStart
        ans = [[row, col]]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        step = 1 
        
        while len(ans) < rows * cols:
            for d in range(4):
                dr, dc = directions[d]
                for _ in range(step):
                    row += dr
                    col += dc
                    
                    if 0 <= row < rows and 0 <= col < cols:
                        ans.append([row, col])
                        
                        if len(ans) == rows * cols:
                            return ans
                        
                if d % 2 == 1:
                    step += 1
        
        return ans
