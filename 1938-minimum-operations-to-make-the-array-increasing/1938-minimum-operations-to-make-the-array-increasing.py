class Solution:
    def minOperations(self, nums: List[int]) -> int:
        moves = 0
        mx = nums[0]
        for v in nums[1:]:
            if v <= mx:
                moves += mx - v +1
                mx += 1
            else:
                mx = v
        return moves