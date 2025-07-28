class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        expected = 1
        for num in arr:
            if num >= expected:
                expected += 1
        return expected - 1
