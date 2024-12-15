class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = "".join(sorted(s))  # Sort string s


        sorted_t = "".join(sorted(t))  # Sort string t

        i, j = 0, 0
        result = []

        while i < len(sorted_t) and j < len(sorted_s):
            if sorted_t[i] == sorted_s[j]:
        # Characters match, move both pointers
                i += 1
                j += 1
            else:
        # Character in t does not match s, append to result
                result.append(sorted_t[i])
                i += 1  # Move pointer in t

# If there's still an extra character left in sorted_t
        while i < len(sorted_t):
            result.append(sorted_t[i])
            i += 1
        return ''.join(result)
