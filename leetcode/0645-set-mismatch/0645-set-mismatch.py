class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing =duplicate= None
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate = nums[i]
            else:
                seen.add(nums[i])
            
            if (i+1) not in seen:
                missing = i+1
        return [duplicate,missing]