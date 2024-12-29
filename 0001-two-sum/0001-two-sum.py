class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the difference and its index
        num_map = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the current number and its index in the dictionary
            num_map[num] = i
