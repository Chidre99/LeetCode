class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        left, right = 0, (len(nums) + 1) // 2
        for i in range(len(nums)):
            if i % 2 == 0:
                res[i] = nums[left]
                left += 1
            else:
                res[i] = nums[right]
                right += 1
        return res
