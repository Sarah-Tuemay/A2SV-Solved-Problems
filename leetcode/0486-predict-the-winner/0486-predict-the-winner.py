class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(left, right):
            if left == right:
                return nums[left]
            
            left_side = nums[left] - dfs(left+1, right)
            right_side = nums[right] - dfs(left, right-1)

            return max(left_side, right_side)

        return dfs(0, len(nums)-1)>=0