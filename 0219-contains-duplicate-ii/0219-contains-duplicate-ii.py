class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            if num in num_indices:
                # Check if the difference in indices is <= k
                if i - num_indices[num] <= k:
                    return True
            # Update the last seen index for the current number
            num_indices[num] = i
        
        # If no such pair is found, return False
        return False
