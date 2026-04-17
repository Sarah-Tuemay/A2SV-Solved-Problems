class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                idx = nums[i]-1
                nums[idx], nums[i] = nums[i], nums[idx]
            
        res = []

        for j in range(len(nums)):
            if nums[j] != j+1:
                res.append(nums[j])
            
        return res