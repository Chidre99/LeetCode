class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with 0s
        stack = []  # Monotonic decreasing stack to store indices

        # Iterate through each day
        for i, current_temp in enumerate(temperatures):
            # Check if the current temperature is warmer than the temperatures in the stack
            while stack and temperatures[stack[-1]] < current_temp:
                prev_index = stack.pop()  # Get the index of the colder day
                result[prev_index] = i - prev_index  # Calculate the difference in days
            
            # Push the current index onto the stack
            stack.append(i)

        return result
