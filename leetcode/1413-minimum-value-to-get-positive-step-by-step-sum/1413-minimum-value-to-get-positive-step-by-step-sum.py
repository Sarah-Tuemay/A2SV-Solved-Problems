class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_value = 1
        sum1 = start_value

        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 < 1:
                start_value += (1-sum1)
                sum1+=(1-sum1)
        

        return start_value