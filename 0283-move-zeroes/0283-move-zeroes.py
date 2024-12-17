class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0  # Position to place the next non-zero element
    
    # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
    
    # Fill the rest of the list with zeroes
        for i in range(pos, len(nums)):
            nums[i] = 0
        