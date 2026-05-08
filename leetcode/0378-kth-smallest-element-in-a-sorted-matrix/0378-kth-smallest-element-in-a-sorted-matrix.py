class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []

        for i in range(len(matrix)):
            arr.extend(matrix[i])
        
        heapify(arr)
        for i in range(k-1):
            heappop(arr)
        
        return heappop(arr)
