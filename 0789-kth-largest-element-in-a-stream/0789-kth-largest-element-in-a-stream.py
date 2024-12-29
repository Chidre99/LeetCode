class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Initialize a min-heap with at most k elements
        self.min_heap = nums
        heapify(self.min_heap)  # Convert nums to a heap
        # If the heap has more than k elements, reduce it
        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heappush(self.min_heap, val)
        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        # The smallest element in the heap is the kth largest
        return self.min_heap[0]
