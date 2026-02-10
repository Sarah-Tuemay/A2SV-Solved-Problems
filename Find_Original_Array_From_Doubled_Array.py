from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        changed_dict = {}
        counted = Counter(changed)
        changed.sort()
        for num in changed:
            changed_dict[num] = 2 * num        
        ans = []

        for i in range(len(changed)):
            if changed[i] == 0:
                if counted[0] >= 2:
                    ans.append(0)
                    counted[0] -= 2
            else:
                if changed[i] in changed_dict and counted[changed[i]] > 0:
                    if changed_dict[changed[i]] in changed_dict and counted[changed_dict[changed[i]] ] >0:
                        ans.append(changed[i])
                        counted[changed_dict[changed[i]]]-=1
                        counted[changed[i]] -= 1
            if len(ans) == len(changed) / 2:
                    return ans
        else:
            return []
