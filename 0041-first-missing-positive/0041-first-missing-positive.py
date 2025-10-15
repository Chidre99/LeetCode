class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present = {}
        for num in nums:
            if num > 0:
                present[num] = True
        i = 1
        while True:
            if i not in present:
                return i
            i += 1
