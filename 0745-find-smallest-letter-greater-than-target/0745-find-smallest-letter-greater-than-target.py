class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        low, high = 0, len(letters) - 1
        result = letters[0]  # Default to the smallest character for wrap-around

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                result = letters[mid]  # Update the result to the potential answer
                high = mid - 1  # Search the left half
            else:
                low = mid + 1  # Search the right half

        return result
            