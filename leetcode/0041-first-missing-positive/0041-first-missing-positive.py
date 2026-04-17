class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] <= len(nums) and nums[i] > 0 and nums[i] != nums[nums[i]-1]:
                idx = nums[i]-1
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                continue
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        
        return len(nums)+1
        # nums.sort()
        # num, prev = 1,0

        # for i in range(0, len(nums)):
        #     if nums[i] <= num:
        #         if nums[i] > 0:
        #             prev = nums[i]
        #     else:
        #         if prev + 1 != nums[i]:
        #             return prev+1
        #         else:
        #             num += 1
        #             prev = nums[i]
        
        # return 1 if prev == 0 else prev+1
            
        