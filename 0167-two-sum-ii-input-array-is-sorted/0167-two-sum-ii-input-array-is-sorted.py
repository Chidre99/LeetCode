class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left, right = 0, len(numbers) - 1
        
        while left < right:
            # Calculate the sum of the numbers at the two pointers
            current_sum = numbers[left] + numbers[right]
            
            # Check if the sum matches the target
            if current_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                # Move the left pointer to increase the sum
                left += 1
            else:
                # Move the right pointer to decrease the sum
                right -= 1
        
        # If no solution exists (should not happen for valid input)
        return []
