class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(queens, xy_diff, xy_sum):
            p = len(queens)

            if p == n:
                res.append(queens)
                return 
            
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens+[q], xy_diff + [p-q] , xy_sum + [p+q])
            
        
        res = []
        backtrack([], [], [])

        return len(res)