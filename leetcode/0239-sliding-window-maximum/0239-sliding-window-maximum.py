class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        queue = deque()

        for right in range(len(nums)):

            while right-left+1 > k:
                if nums[left] == nums[queue[0]]:
                    queue.popleft()
                left += 1

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)   
            
            if right-left+1 == k:
                ans.append(nums[queue[0]])
        
        return ans