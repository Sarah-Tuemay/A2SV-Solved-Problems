class Solution(object):
    def restoreString(self, s, indices):
        mapped_dict = {}

        for i in range(len(indices)):
            mapped_dict[indices[i]] = s[i]

        ans = ""

        for i in range(len(indices)):
            ans += mapped_dict[i]
        
        return ans
