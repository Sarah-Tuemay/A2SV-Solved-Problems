class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        N = len(heights)
        
        for i in range(N - 1):
            if heights[i] < heights[i+1]:
                heapq.heappush(heap, heights[i+1] - heights[i])
                
                if len(heap) > ladders:
                    curr = heapq.heappop(heap)
                    if curr <= bricks:
                        bricks -= curr
                    else:
                        return i
        return N - 1