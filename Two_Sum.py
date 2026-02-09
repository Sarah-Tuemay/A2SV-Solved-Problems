class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in my_dict and my_dict[target-nums[i]] != i:
                ans = []
                ans.append(i)
                ans.append(my_dict[target - nums[i]])
                return ans
