from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative values to simulate a max-heap
        max_heap = [-stone for stone in stones]
        heapify(max_heap)  # Heapify the list to create a heap

        # Continue until there is one or no stone left
        while len(max_heap) > 1:
            # Remove the two largest stones
            stone1 = -heappop(max_heap)  # Largest stone
            stone2 = -heappop(max_heap)  # Second largest stone

            # If they are not the same weight, push the difference back into the heap
            if stone1 != stone2:
                heappush(max_heap, -(stone1 - stone2))

        # If there is a stone left, return its weight, otherwise return 0
        return -max_heap[0] if max_heap else 0
