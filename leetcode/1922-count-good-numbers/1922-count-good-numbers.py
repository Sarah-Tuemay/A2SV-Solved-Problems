class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = n//2
        if n%2 == 0:
            return ((pow(5, m,(10**9 + 7)) * pow(4, m,(10**9 + 7))))%(10**9 + 7)
        else:
            return (pow(5, m+1,(10**9 + 7)) * pow(4, m,(10**9 + 7)))%(10**9 + 7)
