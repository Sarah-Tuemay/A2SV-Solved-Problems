class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        left1 = 0
        left2 = 0
        sum1 = 0
        sum2 = 0
        count1 = 0
        count2 = 0

        for right in range(len(nums)):
            sum1 += nums[right]
            sum2 += nums[right]

            while sum1 > goal:
                sum1 -= nums[left1]
                left1+=1
            
            while left2 < len(nums) and sum2 > goal-1:
                sum2 -= nums[left2]
                left2 += 1
            
            count1 += (right-left1+1)
            count2 += (right-left2+1)
        
        if goal == 0:
            return count1
        return count1 - count2
