class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a = 0
        b = 1
        c = 2
        ans = 0
        nums.sort()
        while c < len(nums):
            if nums[a] + nums[b] > nums[c] and nums[b]+nums[c] > nums[a] and nums[a]+nums[c] > nums[b]:
                if nums[a]+nums[b]+nums[c] > ans:
                    ans = nums[a]+nums[b]+nums[c]

            a +=1
            b +=1
            c +=1
        
        return ans
