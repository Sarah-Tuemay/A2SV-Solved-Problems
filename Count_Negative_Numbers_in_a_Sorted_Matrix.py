class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < 0:
                    count += 1
        
        return count
