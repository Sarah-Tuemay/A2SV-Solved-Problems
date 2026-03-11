class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1            
                nums[i+1] = 1 if nums[i+1] == 0 else 0
                nums[i+2] = 1 if nums[i+2] == 0 else 0
                ans += 1
        
        if 0 in nums:
            return -1
        return ans
