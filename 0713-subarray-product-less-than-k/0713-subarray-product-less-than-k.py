class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        product = 1
        count = 0
        size = len(nums)
        for j in range(size):
            if k<1:
                return 0
            product = product * nums[j]
            while product >= k and i<=j:
                product = product/ nums[i]
                i = i+1
            count = count + (j - i +1)
        return count