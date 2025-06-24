class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count = count + 1
            else:
                continue
        return count