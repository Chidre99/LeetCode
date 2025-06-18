class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if any(total[c] < k for c in 'abc'):
            return -1

        n = len(s)
        max_len = 0
        left = 0
        curr = Counter()

        for right in range(n):
            curr[s[right]] += 1
            while any(total[c] - curr[c] < k for c in 'abc'):
                curr[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len
