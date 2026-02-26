# from collections import defaultdict
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        zero_count = 0
        if 0 not in nums:
            return len(nums)-1
            
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count+=1
            else:
                ans = max(ans, right-left+1-zero_count)

            while zero_count == 2:
                if nums[left] == 0:
                    zero_count-=1
                left+=1
            
        return ans
