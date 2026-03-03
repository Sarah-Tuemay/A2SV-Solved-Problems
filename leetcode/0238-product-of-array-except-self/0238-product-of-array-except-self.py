class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_p = [1] * len(nums)
        suf_p = [1] * len(nums)

        for i in range(1, len(pre_p)):
            pre_p[i] = pre_p[i-1] * nums[i-1]
        
        for i in range(len(suf_p)-2, -1, -1):
            suf_p[i] = suf_p[i+1] * nums[i+1]
        
        ans = [1] * len(nums)

        for i in range(len(ans)):
            ans[i] = pre_p[i] * suf_p[i]
        
        return ans