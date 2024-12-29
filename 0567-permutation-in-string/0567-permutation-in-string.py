from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 longer than s2
        if len(s1) > len(s2):
            return False
        
        # Frequency map for s1
        s1_count = Counter(s1)
        # Frequency map for the current window in s2
        window_count = Counter()
        
        # Sliding window
        for i in range(len(s2)):
            # Add the current character to the window
            window_count[s2[i]] += 1
            
            # If the window size exceeds the size of s1, remove the leftmost character
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1
            
            # Compare the two frequency maps
            if window_count == s1_count:
                return True
        
        return False
