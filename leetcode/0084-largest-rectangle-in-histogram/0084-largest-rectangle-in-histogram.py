class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_ = 0
        # j = 0
        for i in range(len(heights)):
            j = i
            while stack and heights[i] < stack[-1][0]:
                max_ = max(max_, stack[-1][0] * (i - stack[-1][1]))
                j = stack[-1][1]
                stack.pop()
            
            stack.append([heights[i], j])
        
        while stack:
            max_ = max(max_, stack[-1][0] * (len(heights)-stack[-1][1]))
            stack.pop()
        return max_
