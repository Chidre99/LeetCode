class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize variables
        char_count = defaultdict(int)  # Frequency map
        max_length = 0  # Maximum length of valid substring
        max_freq = 0  # Maximum frequency of any character in the window
        left = 0  # Left pointer for the sliding window
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # Increment the count of the current character
            char_count[s[right]] += 1
            # Update max_freq
            max_freq = max(max_freq, char_count[s[right]])
            
            # Check if the current window is valid
            if (right - left + 1) - max_freq > k:
                # Shrink the window from the left
                char_count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length
