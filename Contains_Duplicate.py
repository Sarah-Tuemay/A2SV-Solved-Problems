from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        nums_count = Counter(nums)

        for key in nums_count:
            if nums_count[key] >= 2:
                return True
        return False
