class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        min_ = 0

        pre_sum = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            max_ = max(pre_sum-min_, max_)
            min_ = min(pre_sum, min_)
            
        return max_