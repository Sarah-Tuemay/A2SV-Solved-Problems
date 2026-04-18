class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n - 1)):
            return ""
        
        ans = []
        cnt = 0

        def backtrack(curr):
            nonlocal cnt, ans
            
            if len(curr) == n:
                cnt += 1 
                
                if cnt == k:
                    ans = curr.copy() 
                    return True       
                return False           
            
            for i in ['a', 'b', 'c']:
                
                if not curr or curr[-1] != i:
                    curr.append(i)
                    
                    if backtrack(curr):
                        return 
                    curr.pop()
            

        backtrack([])
        return "".join(ans)