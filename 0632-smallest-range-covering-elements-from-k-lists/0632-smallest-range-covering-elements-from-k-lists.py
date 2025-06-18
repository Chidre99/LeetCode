from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_val = float('-inf')
        
        for i, row in enumerate(nums):
            heapq.heappush(heap, (row[0], i, 0))
            max_val = max(max_val, row[0])

        result = [float('-inf'), float('inf')]

        while True:
            min_val, row_i, col_i = heapq.heappop(heap)
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]

            if col_i + 1 == len(nums[row_i]):
                break

            next_val = nums[row_i][col_i + 1]
            heapq.heappush(heap, (next_val, row_i, col_i + 1))
            max_val = max(max_val, next_val)

        return result
