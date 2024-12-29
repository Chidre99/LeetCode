class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        char_set = set()  # Set to store unique characters
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Maximum length of substring
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the set, shrink the window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
