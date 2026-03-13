class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        i = 0
        nums = []
        num = target
        while i < maxDoubles and num > 1:
            nums.append(num//2)
            num //= 2
            i+=1
        nums.sort() 
        j = 0
        x = 1
        cnt = 0
        while x < target and j < len(nums):
            if x < nums[j]:
                cnt += (nums[j]-x)
                x += (nums[j]-x)
            elif x == nums[j]:
                x*=2
                j += 1
                cnt += 1
        
        if x < target:
            cnt+=(target-x)
        return cnt

