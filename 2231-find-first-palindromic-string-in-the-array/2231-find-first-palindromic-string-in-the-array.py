class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            reversed_word = word[::-1]
            if word == reversed_word:
                return word

        # If no palindrome is found, return an empty string
        return ""
