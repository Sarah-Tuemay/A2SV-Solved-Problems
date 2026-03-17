class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [a+1 for a in range(n)]

        i=0
        while len(arr) > 1:
            i = (i+k-1)%len(arr)
            arr.pop(i)
        
        return arr[0]