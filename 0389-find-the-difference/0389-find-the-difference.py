class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = "".join(sorted(s))


        sorted_t = "".join(sorted(t))
        i, j = 0, 0
        result = []
        while i < len(sorted_t):
    # If j is out of bounds or characters don't match
            if j >= len(sorted_s) or sorted_t[i] != sorted_s[j]:
                result.append(sorted_t[i])
                i += 1
            else:
                i += 1
                j += 1

        return "".join(result)
