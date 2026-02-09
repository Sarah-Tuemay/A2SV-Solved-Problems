class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        ans  = sum(x for x in nums if x%2 == 0)
        print(ans)
        res = []
        for val, index in queries:
            if nums[index] % 2 == 0: 
                ans -= nums[index]  
            nums[index] += val
            if nums[index] % 2 == 0:
                ans += nums[index]
            res.append(ans)
        return res
