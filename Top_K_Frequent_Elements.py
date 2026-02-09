from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dict = Counter(nums)
        nums_dict = dict(sorted(nums_dict.items(), key=lambda item:item[1], reverse=True))
        ans = []
        i = 0
        while i < k:
            first_key = next(iter(nums_dict))
            ans.append(first_key)
            del nums_dict[first_key]
            i+=1

        return ans
