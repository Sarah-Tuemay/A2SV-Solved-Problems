class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        my_dict = defaultdict(int)
        my_dict[0] = -1
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 % k in my_dict:
                if i - my_dict[sum1%k] >= 2:
                    return True
            else:
                my_dict[sum1%k] = i
        
        return False