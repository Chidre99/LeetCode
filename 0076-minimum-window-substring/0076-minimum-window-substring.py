class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Frequency map for t
        t_count = Counter(t)
        required = len(t_count)
        
        # Sliding window variables
        window_count = {}
        left, right = 0, 0
        formed = 0
        min_len = float('inf')
        result = (0, 0)  # (start, end) of the minimum window
        
        while right < len(s):
            # Add the current character to the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if the character matches the count in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window from the left
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if this window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)
                
                # Remove the character from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            # Expand the window
            right += 1
        
        start, end = result
        return s[start:end+1] if min_len != float('inf') else ""
