class Solution(object):
    def isHappy(self, n):
        visited = set()
        
        while True:
            visited.add(n)
            new_num = 0
            while n >= 10:
                new_num += (n % 10) ** 2
                n //= 10 
            new_num += (n ** 2)
            n = new_num

            if new_num == 1:
                return True

            if new_num in visited:
                return False
