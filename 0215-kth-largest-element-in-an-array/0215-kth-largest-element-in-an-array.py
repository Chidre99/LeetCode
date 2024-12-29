class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap of size k
        min_heap = []
        
        for num in nums:
            heappush(min_heap, num)
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heappop(min_heap)
        
        # The root of the heap is the kth largest element
        return min_heap[0]
