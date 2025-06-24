class Solution:
    def maxPower(self, s: str) -> int:
        best = cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                best = max(best, cur)
                cur = 1
        return max(best, cur)