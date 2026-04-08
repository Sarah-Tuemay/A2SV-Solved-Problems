class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def numOfCandies(num):
            candy = 0
            for i in range(len(candies)):
                candy += (candies[i]//num)
            # print(num, candy)
            return candy >= k
        
        low = 1
        high = max(candies)+1

        while low + 1< high:

            mid = (low+high)//2

            if numOfCandies(mid):
                low = mid
            else:
                high = mid
        
        return low