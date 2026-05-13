class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        self.nums.sort()
        if k <= len(nums):
            self.heap = self.nums[len(nums)-k:]
        else:
            self.heap = nums
        

    def add(self, val: int) -> int:
        
        if self.k > len(self.heap):
            heappush(self.heap,val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)

        return self.heap[0]
        



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)