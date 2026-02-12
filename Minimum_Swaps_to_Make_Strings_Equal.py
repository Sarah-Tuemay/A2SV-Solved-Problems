from collections import Counter
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        if len(s1) != len(s2):
            return -1
        
        s1_misplaced = []
        s2_misplaced = []

        ans = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1_misplaced.append(s1[i])
                s2_misplaced.append(s2[i])
        

        s1_misplaced_count = Counter(s1_misplaced)
        s2_misplaced_count = Counter(s2_misplaced)
        
        while s1_misplaced_count["x"] >= 2 and s2_misplaced_count["y"] >= 2:
            ans += 1
            s1_misplaced_count["x"] -= 2
            s2_misplaced_count["y"] -= 2
        
        while s1_misplaced_count["y"] >= 2 and s2_misplaced_count["x"] >= 2:
            ans += 1
            s1_misplaced_count["y"] -= 2
            s2_misplaced_count["x"] -= 2
        
        if s1_misplaced_count["x"] == 1 and s1_misplaced_count["y"] == 1 and s2_misplaced_count["y"] == 1 and s2_misplaced_count["x"] == 1:
            ans += 2
            s1_misplaced_count["x"] -= 1
            s2_misplaced_count["y"] -= 1
            s1_misplaced_count["y"] -= 1
            s2_misplaced_count["x"] -= 1
        
        for key in s1_misplaced_count:
            if s1_misplaced_count[key] != 0:
                return -1
        for key in s2_misplaced_count:
            if s2_misplaced_count[key] != 0:
                return -1

        
        return ans
