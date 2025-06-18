class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            res += count[prefix_sum - goal]
            count[prefix_sum] += 1

        return res
