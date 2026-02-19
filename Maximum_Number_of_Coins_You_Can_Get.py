class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles)-1
        my_pile = 0

        while j > 0 and i < j:
            my_pile += piles[j-1]
            j-=2
            i+=1
          
        return my_pile
