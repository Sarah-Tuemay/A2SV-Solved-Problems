class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(start, comb):
            ans.append(comb[:])

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()
            
        backtrack(0,[])
        return ans
        #     if start == len(nums):
        #         if sorted(comb) not in seen:
        #             ans.append(comb[:])
        #         seen.append(sorted(comb[:]))
        #         return 
            
        #     comb.append(nums[start])
        #     backtrack(start+1, comb)
        #     comb.pop()
        #     backtrack(start+1, comb)
        
        # backtrack(0,[])
        # return ans