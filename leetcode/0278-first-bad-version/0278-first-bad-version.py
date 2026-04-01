# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        ans = 0
        while low <= high:
            mid = (high+low)//2
            if isBadVersion(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid+1
        
        return ans

        