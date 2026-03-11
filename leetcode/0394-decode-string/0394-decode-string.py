class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s)-1
        while i >= 0:
            if s[i].isdigit():
                word = []
                num = []
                while s[i].isdigit():
                    num.append(s[i])
                    i-=1

                while stack and stack[-1] != "]":
                    if stack[-1] != '[':
                        word.append(stack.pop())
                    else:
                        stack.pop()

                if stack:
                    stack.pop()

                stack.append(int("".join(reversed(num))) *"".join(word))
                
            else:
                stack.append(s[i])
                i-=1
                
        ans = ""
        while stack:
            ans += stack.pop()
        
        return ans
                

