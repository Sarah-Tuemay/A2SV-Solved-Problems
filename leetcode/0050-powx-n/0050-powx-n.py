class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            ans = self.myPow(x, abs(n)//2)
            ans*=ans
        else:
            ans = self.myPow(x, abs(n)//2)
            ans *= (ans * x)
        
        if n < 0:
            ans = 1/ ans
        
        return ans