class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = 0
        odd_count = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            res += count[odd_count - k]
            count[odd_count] += 1

        return res
