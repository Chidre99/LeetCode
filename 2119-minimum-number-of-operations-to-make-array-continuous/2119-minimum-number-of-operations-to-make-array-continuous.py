class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        res = n
        for i in range(len(nums)):
            end = nums[i] + n - 1
            j = bisect_right(nums, end)
            window_size = j - i
            res = min(res, n - window_size)
        return res
