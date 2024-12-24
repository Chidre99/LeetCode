class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        i = 0
        j = size-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j = mid-1
            elif target > nums[mid]:
                i = mid + 1
        return -1 