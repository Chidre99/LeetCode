class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        positives = [num for num in unique_nums if num > 0]
        
        if positives:
            return sum(positives)
        elif 0 in unique_nums:
            return 0
        else:
            return max(unique_nums)
