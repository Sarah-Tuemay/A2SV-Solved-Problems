class Solution(object):
    def longestConsecutive(self, nums):
        my_nums = set(nums)
        my_nums = list(my_nums)
        my_nums.sort()
        left = 0
        right = 1
        ans = 1
        res = 1
        if len(nums) == 0:
            return 0
        while right < len(my_nums):
            if my_nums[right] == my_nums[left]+1:
                ans+=1
            else:
                res = max(res, ans)
                ans = 1
            if right == len(my_nums)-1:
                res = max(res, ans)
            left += 1
            right += 1
        return res
