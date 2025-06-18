class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        res = 0
        left, right = 0, len(nums) - 1
        pow2 = [1] * (len(nums))
        for i in range(1, len(nums)):
            pow2[i] = pow2[i - 1] * 2 % mod
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % mod
                left += 1
            else:
                right -= 1
        return res
