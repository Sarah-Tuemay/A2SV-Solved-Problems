class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = nums.copy()
        sorted_nums.sort()

        my_dict = {}
        ans = []
        count = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in my_dict:
                my_dict[sorted_nums[i]] = count
                count += 1
            else:
                count += 1
                
        for i in range(len(nums)):
            ans.append(my_dict[nums[i]])

        
        return ans
                
