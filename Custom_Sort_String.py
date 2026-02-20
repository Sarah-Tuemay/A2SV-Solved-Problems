class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""

        s_dict = Counter(s)

        for ch in order:
            if ch in s_dict:
                ans += ch * s_dict[ch]
                s_dict[ch] = 0
        
        for key in s_dict:
            if s_dict[key] > 0:
                ans += key * s_dict[key]
        
        # print(ans)
        return ans
