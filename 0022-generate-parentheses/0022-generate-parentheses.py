class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # Helper function for backtracking
        def backtrack(current, open_count, close_count):
            # Base case: When the combination is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening parenthesis if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add a closing parenthesis if valid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Start the recursion
        backtrack("", 0, 0)
        return result
