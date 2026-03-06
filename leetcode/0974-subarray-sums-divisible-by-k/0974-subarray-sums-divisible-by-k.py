class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_dict= defaultdict(int)
        my_dict[0] = 1

        sum1 = 0
        ans = 0

        for i in range(len(nums)):
            sum1+= nums[i]
            if sum1%k in my_dict:
                ans += my_dict[sum1%k]
            my_dict[sum1%k] += 1

        return ans
            
