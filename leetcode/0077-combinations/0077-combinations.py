class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backTrack(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
            
            for nc in range(start, n+1):
                comb.append(nc)
                backTrack(nc+1, comb)
                comb.pop()
            
        backTrack(1,[])
        return ans

        