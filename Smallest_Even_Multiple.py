class Solution(object):
    def smallestEvenMultiple(self, n):        
        for i in range(n, 300):
            if i % 2 == 0 and i % n == 0:
                return i
