from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        strs_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            strs_dict[sorted_word].append(word)
        
        ans = []
        for key in strs_dict:
            ans.append(strs_dict[key])
        return ans
