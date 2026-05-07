from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N = len(stones)
        for i in range(N):
            stones[i] = -stones[i]
        
        heapify(stones)

        while len(stones) > 1:
            num1 = heappop(stones)
            num2 = heappop(stones)
            if num1 != num2:
                heappush(stones, num1-num2)
        
        if not stones:
            return 0
        return 0-stones[0]