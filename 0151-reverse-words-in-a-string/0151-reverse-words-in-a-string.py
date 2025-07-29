class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        word.reverse()
        reverse_word = ' '.join(word)
        return reverse_word.strip(" ")