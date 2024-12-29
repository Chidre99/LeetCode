class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a max-heap of size k
        max_heap = []

        for x, y in points:
            # Calculate the distance squared from the origin
            distance = -(x**2 + y**2)  # Use negative to simulate a max-heap
            if len(max_heap) < k:
                heappush(max_heap, (distance, [x, y]))
            else:
                heappushpop(max_heap, (distance, [x, y]))  # Maintain heap size k

        # Extract the points from the heap
        return [item[1] for item in max_heap]
