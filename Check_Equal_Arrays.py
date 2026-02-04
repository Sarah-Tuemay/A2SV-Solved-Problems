class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False
