class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(queens, xy_diff, xy_sum):
            p = len(queens)

            if p == n:
                board = []
                for i in range(n):
                    q = ['.']*n
                    q[queens[i]] = 'Q'
                    board.append(q)
                res.append(board)
                return 
            
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens + [q], xy_diff + [p-q], xy_sum + [p+q])
        
        res = []
        backtrack([],[],[])
        ans = []
        for i in range(len(res)):
            q = []
            for j in res[i]:

                q.append("".join(j))
            ans.append(q)

        return ans

