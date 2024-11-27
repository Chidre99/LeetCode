class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any trailing spaces from the string
        s = s.strip()
        
        # Split the string into a list of words
        words = s.split()
        
        # Return the length of the last word
        return len(words[-1])