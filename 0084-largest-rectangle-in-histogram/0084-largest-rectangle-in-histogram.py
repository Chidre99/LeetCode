class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Monotonic increasing stack (stores indices)
        max_area = 0  # Variable to store the maximum rectangle area
        n = len(heights)
        
        # Traverse the histogram
        for i in range(n):
            # While the stack is not empty and the current height is smaller than the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar at the top of the stack
                # Calculate the width
                width = i if not stack else i - stack[-1] - 1
                # Update the maximum area
                max_area = max(max_area, h * width)
            # Push the current index onto the stack
            stack.append(i)
        
        # Process remaining bars in the stack
        while stack:
            h = heights[stack.pop()]  # Height of the bar at the top of the stack
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area
