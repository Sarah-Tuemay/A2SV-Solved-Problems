from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        nums_dict = Counter(nums)

        n = len(nums) // 3
        ans = []

        for key in nums_dict:
            if nums_dict[key] > n:
                ans.append(key)
        return ans

        
