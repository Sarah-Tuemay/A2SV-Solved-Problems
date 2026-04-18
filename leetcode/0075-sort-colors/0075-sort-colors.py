class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0 = nums.count(0)
        cnt1 = nums.count(1)
        cnt2 = nums.count(2)

        for i in range(len(nums)):
            if 0 <= i < cnt0:
                nums[i] = 0

            elif cnt0 <= i < cnt0+cnt1:
                nums[i] = 1
            else:
                nums[i] = 2