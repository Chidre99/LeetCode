class MedianFinder:

    def __init__(self):
        # Min-heap to store the larger half of the numbers
        self.min_heap = []
        # Max-heap (inverted values) to store the smaller half of the numbers
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # Add to max-heap (negative value for max-heap behavior)
        heapq.heappush(self.max_heap, -num)

        # Balance heaps: Ensure the smallest value in the max-heap moves to the min-heap
        if self.max_heap and self.min_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Balance sizes: Ensure the size difference between heaps is at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If the sizes are equal, the median is the average of the roots
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # If not, the median is the root of the larger heap
        return -self.max_heap[0]

# Example usage:
# medianFinder = MedianFinder()
# medianFinder.addNum(1)
# medianFinder.addNum(2)
# print(medianFinder.findMedian())  # Output: 1.5
# medianFinder.addNum(3)
# print(medianFinder.findMedian())  # Output: 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()