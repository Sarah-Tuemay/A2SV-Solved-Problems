from collections import defaultdict
class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        my_dict = defaultdict(list)

        ans = 0
        for i in range(len(nums)):
            my_dict[nums[i]].append(i)

        for key in my_dict:
            key_list = my_dict[key]

            for i in range(len(key_list)):
                for j in range(i+1, len(key_list)):
                    if key_list[i] * key_list[j] % k == 0:
                        ans += 1
        return ans
