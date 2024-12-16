class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        
        # Traverse from the last digit to the first digit
        for i in range(size - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If all digits are 9, add a leading 1 (e.g., 999 -> 1000)
        return [1] + digits
