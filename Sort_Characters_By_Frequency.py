from collections import Counter
class Solution:
    
    def frequencySort(self, s: str) -> str:
        ans = ""
        s_str = Counter(s)
        s_str = dict(sorted(s_str.items(), key=lambda item:item[1], reverse=True))
        for key in s_str:
            ans += key*s_str[key]
        
        return ans
