from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0  

        for row in grid:
            low, high = 0, len(row) - 1

            while low <= high:
                mid = (low + high) // 2
                if row[mid] < 0:  
                    high = mid - 1  
                else:  
                    low = mid + 1

            
            count += len(row) - low

        return count
