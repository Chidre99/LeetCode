class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = sorted(x for x in nums if x % 2)
        nums_even = sorted(x for x in nums if x % 2 == 0)
        target_odd = sorted(x for x in target if x % 2)
        target_even = sorted(x for x in target if x % 2 == 0)

        total_moves = 0
        for a, b in zip(nums_odd, target_odd):
            total_moves += abs(a - b) // 2
        for a, b in zip(nums_even, target_even):
            total_moves += abs(a - b) // 2
        
        return total_moves // 2
