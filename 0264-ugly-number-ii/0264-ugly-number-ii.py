import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        for _ in range(n):
            curr = heapq.heappop(heap)
            for f in [2, 3, 5]:
                next_ugly = curr * f
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heapq.heappush(heap, next_ugly)
        return curr
