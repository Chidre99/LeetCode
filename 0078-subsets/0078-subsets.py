class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current_subset):
            # Add the current subset to the result
            result.append(current_subset[:])
            
            # Explore further subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Recurse with the next starting index
                backtrack(i + 1, current_subset)
                # Backtrack by removing the last added element
                current_subset.pop()
        
        # Start the backtracking with an empty subset
        backtrack(0, [])
        return result