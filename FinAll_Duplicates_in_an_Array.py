class Solution(object):
    def findDuplicates(self, nums):
        l = 0
        r = 1
        ans = []
        nums.sort()
        while(l < r and r < len(nums)):
            if nums[l] == nums[r]:
                ans.append(nums[l])
                l += 2
                r += 2
                
            else:
                l += 1
                r += 1
        return ans
