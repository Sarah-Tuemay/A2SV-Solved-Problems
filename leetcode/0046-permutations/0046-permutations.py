class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        choosen = [False] * len(nums)
        def search():

            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            
            for i in range(len(nums)):
                if choosen[i] == True:
                    continue
                
                choosen[i] = True
                perm.append(nums[i])
                search()
                perm.pop()
                choosen[i] = False
        
        search()
        return ans
                