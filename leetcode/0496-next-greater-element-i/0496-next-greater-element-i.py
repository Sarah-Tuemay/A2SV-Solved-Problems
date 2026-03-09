from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = defaultdict(int)
        stack = []

        for i in range(len(nums2)-1,-1, -1):
            if not stack:
                my_dict[nums2[i]] = -1
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                
                if not stack:
                    my_dict[nums2[i]] = -1
                else:
                    my_dict[nums2[i]] = stack[-1]
                
                stack.append(nums2[i])
        
        ans = []
        for i in nums1:
            ans.append(my_dict[i])
        
        return ans