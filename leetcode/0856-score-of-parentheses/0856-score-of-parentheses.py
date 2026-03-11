class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    num = 0
                    while stack[-1] != "(":
                        num+=stack.pop()    
                    stack.pop()
                    stack.append(2*num)
        
        if len(stack) >=2:
            ans = 0
            while stack:
                ans+=stack.pop()
            
            return ans
        
        return stack[0]

                