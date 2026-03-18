class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        i = len(nums)-1
        while i > 0:
            if nums[i-1] > nums[i]:
                x = ceil(nums[i-1]/nums[i])
                ans += x-1
                nums[i-1] = nums[i-1]//x
            else:
                i-=1
        return ans