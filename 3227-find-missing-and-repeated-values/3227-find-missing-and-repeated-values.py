class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        total = n * n
        repeated = -1
        actual_sum = 0
        
        for row in grid:
            for num in row:
                actual_sum += num
                if num in seen:
                    repeated = num
                else:
                    seen.add(num)

        expected_sum = total * (total + 1) // 2
        missing = expected_sum - (actual_sum - repeated)
        
        return [repeated, missing]