class Solution(object):
    def singleNumber(self, nums):
        l = 0
        r = 1
        nums.sort()
        while l < r and r < len(nums)-1:
            if nums[l] == nums[r]:
                l += 2
                r += 2
            else:
                return nums[l]
        else:
            return nums[l]
