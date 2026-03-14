class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_ = float('inf')
        max_ = float('-inf')

        max_stack = deque()
        min_stack = deque()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while max_stack and max_stack[-1] < nums[right]:
                max_stack.pop()
            while min_stack and min_stack[-1] > nums[right]:
                min_stack.pop()
            
            max_stack.append(nums[right])
            min_stack.append(nums[right])
 
            if max_stack[0] - min_stack[0] > limit: 
                if nums[left] == max_stack[0]:
                    max_stack.popleft()
                elif nums[left] == min_stack[0]:
                    min_stack.popleft()
                left += 1
            else:
                ans = max(ans, right-left+1)
            
        
        return ans