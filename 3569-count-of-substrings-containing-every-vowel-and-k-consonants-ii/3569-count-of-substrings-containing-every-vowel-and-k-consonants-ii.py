class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(k_val: int) -> int:
            cnt = Counter()
            ans = l = consonants = 0
            for c in word:
                if c in "aeiou":
                    cnt[c] += 1
                else:
                    consonants += 1
                while consonants >= k_val and len(cnt) == 5:
                    d = word[l]
                    if d in "aeiou":
                        cnt[d] -= 1
                        if cnt[d] == 0:
                            cnt.pop(d)
                    else:
                        consonants -= 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)
