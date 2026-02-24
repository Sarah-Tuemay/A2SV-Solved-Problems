class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = float('-inf')
        left, right = 0, len(height) - 1
        
        while right > left:
            max_ = max(max_, (right - left) * min(height[right], height[left]))
            if height[right] < height[left]:
                right -= 1

            else:
                left += 1
        
        return max_
