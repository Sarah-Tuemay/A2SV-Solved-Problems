class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def back(idx, comb):
            if len(comb) >= 2:
                for i in range(1, len(comb)):
                    if comb[i] < comb[i-1]:
                        return
                
                if tuple(comb) not in seen:
                    seen.add(tuple(comb))
                    ans.append(comb[:])


            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                back(i+1, comb)
                comb.pop()
        
        back(0, [])
        return ans