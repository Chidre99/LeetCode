class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):  # Check all substring lengths up to n//2
            if n % i == 0:  # Only consider lengths that evenly divide n
                substring = s[:i]  # Get the candidate substring
                if substring * (n // i) == s:  # Check if repeating substring reconstructs s
                    return True
        return False
