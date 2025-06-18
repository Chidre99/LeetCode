class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * (n - k + 1)
        left = 0
        
        for right in range(n):
            if nums[right] - nums[left] != right - left:
                left = right
            if right - left + 1 == k:
                res[left] = nums[right]
                left += 1
        
        return res
