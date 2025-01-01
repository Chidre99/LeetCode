class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            # If we have a complete permutation
            if start == len(nums):
                result.append(nums[:])  # Add a copy of nums to the result
                return
            
            # Iterate over the options for the current position
            for i in range(start, len(nums)):
                # Swap the current index with the start index
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse to generate permutations for the next position
                backtrack(start + 1)
                # Undo the swap (backtrack)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result