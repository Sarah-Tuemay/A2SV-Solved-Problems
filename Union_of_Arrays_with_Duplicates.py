class Solution:    
    def findUnion(self, a, b):
        a.extend(b)
        a = set(a)
        return a 
