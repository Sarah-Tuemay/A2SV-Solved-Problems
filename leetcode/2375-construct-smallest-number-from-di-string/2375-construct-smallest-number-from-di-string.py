class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        
        def backtrack(curr, used):
            if len(curr) == N + 1:
                return "".join(curr) 
            
            for i in range(1, N + 2):
                if i not in used:
                    valid = True
                    if curr:
                        rule = pattern[len(curr) - 1]
                        if rule == 'I' and curr[-1] >= str(i):
                            valid = False
                        if rule == 'D' and curr[-1] <= str(i):
                            valid = False
                    
                    if valid:
                        curr.append(str(i))
                        used.add(i)

                        result = backtrack(curr, used)
                        if result:  
                            return result 
                            
                        curr.pop()
                        used.remove(i)
            
            return False

        return backtrack([], set())