class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        return list(anagrams.values())
