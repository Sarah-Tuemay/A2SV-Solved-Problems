class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min_ = float('inf')
        while low <= high:

            mid = (low+high)//2

            if nums[low] <= nums[mid]:
                min_ = min(nums[low], min_)
                low = mid+1
            else:
                min_ = min(nums[mid], min_)
                high = mid-1
        
        return min_
