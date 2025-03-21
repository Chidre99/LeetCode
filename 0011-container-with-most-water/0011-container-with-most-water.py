class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area formed by the two pointers
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
