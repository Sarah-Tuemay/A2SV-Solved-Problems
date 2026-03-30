class Solution:
    def splitString(self, s: str) -> bool:
        curr = []

        def backt(idx):
            if idx >= len(s):
                for i in range(1,len(curr)):
                    if curr[i-1] - curr[i]!=1:
                        return False
                
                return len(curr) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                curr.append(val)
                if backt(i+1):
                    return True
                
                curr.pop()
            
            return False
        return backt(0)
                