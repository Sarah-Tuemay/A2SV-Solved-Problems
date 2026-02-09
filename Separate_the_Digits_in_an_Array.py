class Solution(object):
    def separateDigits(self, nums):
        ans = []
        for num in nums:
            nums_str = str(num)
            for i in range(len(nums_str)):
                ans.append(int(nums_str[i]))
        
        return ans
        
