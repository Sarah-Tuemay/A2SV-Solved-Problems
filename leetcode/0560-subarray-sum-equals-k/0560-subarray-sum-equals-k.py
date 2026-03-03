class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1
        ans = 0
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]

            if pre_sum - k in my_dict:
                ans += my_dict[pre_sum-k]

            my_dict[pre_sum] += 1

        
        return ans