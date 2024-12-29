class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary to group anagrams
        anagrams = {}
        
        for string in strs:
            # Sort the string to get the key
            key = "".join(sorted(string))
            
            # Add the string to the corresponding group
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())
