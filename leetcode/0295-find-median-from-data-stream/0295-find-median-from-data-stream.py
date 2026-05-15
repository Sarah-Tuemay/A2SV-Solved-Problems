class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        if len(self.smaller) <= len(self.larger):
            heappush(self.smaller, -num)
        else:
            heappush(self.larger, num)
        
        if self.smaller and self.larger and -self.smaller[0] > self.larger[0]:
            n,m = self.smaller[0], self.larger[0]
            heapreplace(self.smaller, -m)
            heapreplace(self.larger, -n)

    def findMedian(self) -> float:
        # print(self.smaller[0])
        # print(self.larger[0])
        # print()
        if len(self.smaller) == len(self.larger):
            n, m = self.smaller[0], self.larger[0]
            return (-n+m)/2
        else:
            return -self.smaller[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()