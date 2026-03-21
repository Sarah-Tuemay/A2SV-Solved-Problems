class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        ans = []
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                ans.append(t[i])
                j+=1
        
        return "".join(ans) == s