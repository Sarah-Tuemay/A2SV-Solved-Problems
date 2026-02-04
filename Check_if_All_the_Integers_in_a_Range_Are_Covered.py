class Solution(object):
    def isCovered(self, ranges, left, right):
        for i in range(left, right+1):
            flag = False
            for list in ranges:
                if i in range(list[0], list[1]+1):
                    flag = True
                    break
            
            if not flag:
                return False
        
        return True
