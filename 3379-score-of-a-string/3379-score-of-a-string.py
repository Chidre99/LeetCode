class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(1,len(s)):
            diff = abs(ord(s[i-1]) - ord(s[i]))
            sum = sum +  diff
        return sum