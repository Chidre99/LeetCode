class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Use a dictionary to count character occurrences in the first string
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract character occurrences based on the second string
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        # If all counts are zero, it's an anagram
        return all(value == 0 for value in count.values())
