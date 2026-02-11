from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        my_set = set()
        for num in nums_count:
            if nums_count[num] > len(nums) // 2:
                my_set.add(num)
        if len(my_set) == 0:
            return -1
        could_be_dominant = my_set.pop()
        count = 0
        for i in range(len(nums)):
            if nums[i] == could_be_dominant:
                count += 1
                if count * 2 > (i + 1) and (nums_count[could_be_dominant] - count) * 2 > (len(nums) - (i + 1)):
                    return i
    
        return -1
        
