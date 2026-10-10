class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (negated values)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # push into small, then move small's max over to large
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # rebalance so small is never smaller than large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2