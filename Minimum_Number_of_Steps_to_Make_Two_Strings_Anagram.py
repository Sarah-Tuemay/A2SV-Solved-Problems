from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        for key in s_count:
            if key in t_count:
                if t_count[key] >= s_count[key]:
                    t_count[key] -= s_count[key]
                else:
                    t_count[key] = 0

        ans = 0
        for  key in t_count:
            if t_count[key] != 0:
                ans += t_count[key]
                
        return ans
