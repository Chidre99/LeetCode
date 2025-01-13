class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Helper function to check if a word is a palindrome
        def check_palindrome(word):
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Iterate through the words and return the first palindrome
        for word in words:
            if check_palindrome(word):
                return word

        # If no palindrome is found, return an empty string
        return ""
